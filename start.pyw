from presenter.presenter import TestPresenter
import pandas as pd
from os import listdir
from pathlib import Path


def create_base_file(savepath: Path, filename: str):
        data = pd.DataFrame({"ID": [],"Дата": [],"Вид материала": [], "Размер катушки / вес, кг": [], "Сечение": [], "Цвет": [], "Условия хранения": [], "Статус": [], "Остаток": []})
        excelWriter = pd.ExcelWriter(savepath / filename, engine="openpyxl")
        data.to_excel(excelWriter, sheet_name="Лист 1", index=False)
        excelWriter.close()
        return savepath / filename


WORKING_DIR = Path(__file__).parent
xslxFiles = listdir(WORKING_DIR / "data")
filterdFiles = filter(lambda x: x.split(".")[-1] == "xlsx", xslxFiles)
fullPathes = [WORKING_DIR / "data" / i for i in filterdFiles]
if len(fullPathes) == 0:
        result = create_base_file(WORKING_DIR / "data", "materials.xlsx")
        fullPathes.append(result)
TestPresenter(fullPathes[0])