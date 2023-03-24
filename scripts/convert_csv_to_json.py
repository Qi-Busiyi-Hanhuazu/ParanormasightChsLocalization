#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import csv
import os

DIR_ORIGINAL = "master/texts"
DIR_FILES = "master/files"

languages = os.listdir(DIR_ORIGINAL)

def get_sheet(language: str, sheet_name: str) -> dict[str, str]:
  csvfile = open(f"{language}/{sheet_name}.csv", "r", encoding="utf-8-sig", newline="")
  reader = csv.reader(csvfile)

  row_iter = reader
  next(row_iter)
  msgidx: list[str] = []
  chinese: list[str] = []
  for row in row_iter:
    msgidx.append(row[3])
    chinese.append(row[2] or "")

  return dict(zip(msgidx, chinese))

for language in languages:
  if language in ["ja", "en"]:
    continue

  files = os.listdir(f"{DIR_ORIGINAL}/{language}")
  for file_name in files:
    if not file_name.endswith(".txt"):
      continue

    with open(f"{DIR_ORIGINAL}/ja/{file_name}", "r", -1, "utf-8-sig") as reader:
      original_messages = reader.read().strip("\n").split("\n")
    if len(original_messages) < 1:
      continue

    sheet_name = file_name.removesuffix(".txt")
    chinese = get_sheet(language, sheet_name)

    writer = open(f"{DIR_ORIGINAL}/{language}/{file_name}", "w", -1, "utf-8-sig")

    for line in original_messages:
      msgidx, *_ = line.split(",")
      line = ",".join(_).strip()

      suffix = ""
      if line.endswith("[l][p]"):
        suffix += "[l][p]"
        line = line.removesuffix("[l][p]")
      
      new_line = chinese[msgidx] + suffix
      new_line = new_line.replace("\n", "[r]")
      writer.write(f"{msgidx},{new_line}\n")

    writer.write("\n")
    writer.close()

    character_table = ""
    if os.path.exists(f"{DIR_FILES}/CharacterTable-{language}.txt"):
      with open(f"{DIR_FILES}/CharacterTable-{language}.txt", "r", -1, "utf-8") as reader:
        character_table += reader.read()
    
    character_table += "".join(chinese.values())
    character_table = " 　\n" + "".join(sorted(set(character_table))).strip()

    with open(f"{DIR_FILES}/CharacterTable-{language}.txt", "w", -1, "utf-8") as writer:
      writer.write(character_table)