import tkinter.filedialog
from tkinter import *


root = Tk()
root.withdraw()
files_path = tkinter.filedialog.askopenfilenames()
saves_path = tkinter.filedialog.askdirectory()

for file_path in files_path:
    with open(file_path, 'r', encoding='UTF-8') as fr:
        file_data = fr.read().splitlines()
        dialog_content = []
        for i in range(0, len(file_data)):
            if file_data[i] == "focus":
                dialog_content.append(file_data[i+1])
                dialog_content.append(file_data[i+2])
        adv_content = []
        if len(dialog_content) == 0:
            continue
        new_sentence = "【" + dialog_content[0] + "】"
        cur_chara = dialog_content[0]
        for j in range(0, len(dialog_content), 2):
            if dialog_content[j] == cur_chara:
                new_sentence = new_sentence + dialog_content[j+1]
            else:
                cur_chara = dialog_content[j]
                adv_content.append(new_sentence)
                new_sentence = "【" + dialog_content[j] + "】"
                if j == len(dialog_content)-2:
                    new_sentence = new_sentence + dialog_content[j+1]
        adv_content.append(new_sentence)
        adv_result = []
        for content in adv_content:
            adv_result.append(content.replace("\\n", "") + "\n")
        print(adv_result)
        new_file_name = file_path.split("/")[-1].replace("-rawdata", "")
        with open(saves_path + "/" + new_file_name, 'w', encoding="UTF-8") as fw:
            fw.writelines(adv_result)
