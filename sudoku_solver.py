from sudoku_helper import solve
from selenium import webdriver
from copy import deepcopy
from time import sleep

def get_board(d):
    full_table = d.find_element_by_id("puzzle_grid")
    rows = full_table.find_elements_by_tag_name("tr")
    elements = [row.find_elements_by_tag_name("input") for row in rows]
    for y in range(len(elements)):
        for x in range(len(elements[y])):
            value = elements[y][x].get_attribute("value")
            elements[y][x] = 0 if len(value) == 0 else int(value)
    return elements

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://grid.websudoku.com/?level=4")

while True:
    sleep(1)
    actual_values = get_board(d=driver)
    solved_values = solve(deepcopy(actual_values))
    for y in range(len(actual_values)):
        for x in range(len(actual_values[y])):
            if actual_values[y][x] == 0:
                cell_id = "f" + str(x) + str(y)
                curr_cell = driver.find_element_by_id(cell_id)
                curr_cell.send_keys(str(solved_values[y][x]))
    sleep(1)
    driver.find_element_by_name("submit").click()
    sleep(1)
    driver.find_element_by_name("newgame").click()