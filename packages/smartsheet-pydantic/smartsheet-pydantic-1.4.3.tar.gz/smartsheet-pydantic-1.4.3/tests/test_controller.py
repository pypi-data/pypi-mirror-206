from datetime import date
from unittest.mock import patch, Mock
from smartsheet.models.row import Row

from src.smartsheet_pydantic.controller import \
    SheetDetail, SmartsheetControllerFactory, SmartsheetController
from tests.factories.mock_smartmodel import MockSmartModel
from tests.factories.mock_source import MockSource
from tests.factories.mock_sheet import MockSheet


detail_param = {
    "sheet_id": "0123456789",
    "description": "mock_sheet",
    "smart_model": MockSmartModel,
    "source": MockSource,
}


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
def setup_test_controller(client) -> SmartsheetController:
    client.return_value = Mock()
    sheet_detail = SheetDetail(**detail_param)

    return SmartsheetControllerFactory.get_controller(
        sheet_detail=sheet_detail,
    )


def test_smartsheet_controller_factory_initialization():
    """
    ControllerFactory can properly ingest the SheetDetail and return
    a Controller with the correct attributes.
    """
    test_controller = setup_test_controller()
    assert test_controller.sheet_id == detail_param['sheet_id']
    assert test_controller.description == detail_param['description']
    assert test_controller.smart_model == detail_param['smart_model']


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
@patch('src.smartsheet_pydantic.controller.SmartsheetController._set_sheet')
def test_smartsheet_controller_extract_as_smartmodels(set_sheet, client):
    """
    Given the SheetDetail, the Controller can properly extract data
    from the mock Smartsheet and return a list of validated SmartMOdel.
    """
    client.return_value = Mock()
    data = MockSource().get()
    set_sheet.return_value = MockSheet(data)
    sheet_detail = SheetDetail(**detail_param)

    test_controller = SmartsheetControllerFactory.get_controller(
        sheet_detail=sheet_detail,
    )
    result: set[MockSmartModel] = test_controller.extract_as_smartmodels()
    expected = {
        MockSmartModel(**mock_data) for mock_data
        in MockSource().get()
    }
    assert result == expected


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
@patch('src.smartsheet_pydantic.controller.SmartsheetController._set_sheet')
def test_smartsheet_controller_get_row_ids(set_sheet, client):
    """
    Given the SheetDetail, the Controller can properly extract data
    from the mock Smartsheet and return a list of Smartsheet Python SDK's
    Row object ids.
    """
    client.return_value = Mock()
    data = MockSource().get()
    mock_sheet = MockSheet(data)
    set_sheet.return_value = mock_sheet

    sheet_detail = SheetDetail(**detail_param)
    test_controller = SmartsheetControllerFactory.get_controller(
        sheet_detail=sheet_detail
    )
    actual_row_ids = test_controller._get_row_ids()
    expected_row_ids = [row.id for row in mock_sheet.rows]
    assert actual_row_ids == expected_row_ids


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
@patch('src.smartsheet_pydantic.controller.SmartsheetController._set_sheet')
def test_smartsheet_controller_query_database(set_sheet, client):
    """
    Given the SheetDetail, the Controller can properly query the
    database and return a list of tuples.
    """
    client.return_value = Mock()
    data = MockSource().get()
    mock_sheet = MockSheet(data)
    set_sheet.return_value = mock_sheet

    sheet_detail = SheetDetail(**detail_param)
    test_controller = SmartsheetControllerFactory.get_controller(
        sheet_detail=sheet_detail
    )
    db_data = test_controller._query_database()
    assert db_data == data


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
@patch('src.smartsheet_pydantic.controller.SmartsheetController._set_sheet')
def test_smartsheet_controller_extract_row_objects(set_sheet, client):
    """
    Given the SheetDetail, the Controller can properly extract data
    from the mock Smartsheet and return a list of Smartsheet Python SDK's
    Row object.
    """
    client.return_value = Mock()
    data = MockSource().get()
    mock_sheet = MockSheet(data)
    set_sheet.return_value = mock_sheet

    sheet_detail = SheetDetail(**detail_param)
    test_controller = SmartsheetControllerFactory.get_controller(
        sheet_detail=sheet_detail
    )
    actual_rows: list[Row] = test_controller.extract_row_objects()
    expected_rows: list[Row] = [row for row in mock_sheet.rows]
    assert actual_rows == expected_rows


@patch('tests.test_controller.SmartsheetControllerFactory.return_client')
@patch('src.smartsheet_pydantic.controller.SmartsheetController._set_sheet')
def test_mock_source_substitution(set_sheet, client):
    """
    SheetDetail['source'] is left empty by default, so the source defined
    within SmartModel can be used. However, when testing it is useful to be
    able to override the source with a mock source. Test that the by defining
    a mock source in SheetDetail, it is overriding the source that is being
    used by the controller.
    """
    client.return_value = Mock()
    data = MockSource().get()
    set_sheet.return_value = MockSheet(data)

    detail_default = SheetDetail(
        sheet_id="0123456789",
        description="mock_sheet",
        smart_model=MockSmartModel,
    )

    factory = SmartsheetControllerFactory()
    controller = factory.get_controller(detail_default)
    result: list[dict] = controller._query_database()
    first_model = result[0]
    assert len(result) == 3
    assert first_model['test_field_1'] == 'unique_key_1'
    assert first_model['test_field_2'] == 1
    assert first_model['test_field_3'] == 1.0
    assert first_model['test_field_4'] == '2014-10-01'

    class OverrideSource():
        def get(self):
            return [
                {
                    'test_field_1': 'override',
                    'test_field_2': 10,
                    'test_field_3': 10.0,
                    'test_field_4': date(2023,1,1)
                }
            ]

    detail_with_mock_source_override = SheetDetail(
        sheet_id="0123456789",
        description="mock_sheet",
        smart_model=MockSmartModel,
        source=OverrideSource
    )

    controller = factory.get_controller(detail_with_mock_source_override)
    result = controller._query_database()
    first_model = result[0]
    assert first_model['test_field_1'] == 'override'
    assert first_model['test_field_2'] == 10
    assert first_model['test_field_3'] == 10.0
    assert first_model['test_field_4'] == date(2023, 1, 1)
