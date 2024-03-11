from unittest.mock import MagicMock
import datetime
from Src.reference import reference
from Logics.convert_factory import convert_factory
from Logics.data_presentation import convert
from Storage.storage import storage
from Models.unit_model import unit_model
from Models.nomenclature_model import nomenclature_model
from Src.settings_manager import settings_manager
from Logics.Formats.data_csv import csv_convert
import json
from Logics.start_factory import start_factory
import unittest
from Logics.Formats.data_json import json_convert
class TestSettings(unittest.TestCase):

    """Проверить статический метод build класса convert"""
    def test_convert_build(self):
        #Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]

        #Действие
        result = convert.build(storage.unit_key(), data)

        assert result is not None
        assert len(result) > 0

    def test_check_csv_create(self):
        # Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]
        menager = settings_manager()
        # Действие
        csv = csv_convert(menager.settings, data)

        result = csv.create(storage.unit_key())
        print(result)

        assert result is not None
        assert len(result) > 0

    """Проверить статический метод build класса convert"""
    def test_convert_build_for_nomenclature(self):
        #Подготовка
        data = {}
        data[storage.nomenclature_key()] = [nomenclature_model]

        #Действие
        result = convert.build(storage.nomenclature_key(), data)

        assert result is not None
        assert len(result) > 0

    def test_check_csv_create_for_nomenclature(self):
        # Подготовка
        data = {}
        data[storage.nomenclature_key()] = [nomenclature_model]
        menager = settings_manager()
        # Действие
        csv = csv_convert(menager.settings, data)

        result = csv.create(storage.nomenclature_key())
        print(result)
        """Будут установлены значения по дефолту, поскольку данная модель не заполнена"""

        assert result is not None
        assert len(result) > 0


    def test_check_reporting_json_build(self):
        # Подготовка
        data = {}
        data[storage.unit_key()] = [unit_model.create_unit_gramm()]

        # Действие
        result = json_convert.build(storage.unit_key())

        assert result is not None
        assert len(result) > 0

    def test_check_convert_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        if len(items) == 0:
            raise Exception("Список номенклатуры пуст!")

        item = items[0]

        # Действие
        result = factory.convert(item)

        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys=True, indent=4)

        file = open("nomenclature.json", "w")
        file.write(json_text)
        file.close()

    def test_check_convert_nomenctalures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()

        # Действие
        result = factory.convert(items)

        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys=True, indent=4)

        file = open("nomenclatures.json", "w")
        file.write(json_text)
        file.close()



