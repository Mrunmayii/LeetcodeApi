from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

class Data:
    def __init__(self, username):
        self.__username = username
        
    def get_detail(self):
        url = 'https://leetcode.com/'+ self.__username

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        solved_que = soup.find_all('span', class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1')
        total_que = soup.find_all('span', class_='text-xs font-medium text-label-4 dark:text-dark-label-4')

        easy_questions_solved = solved_que[0].text
        total_easy_questions = total_que[0].text
        medium_questions_solved = solved_que[1].text
        total_medium_questions = total_que[1].text
        hard_questions_solved = solved_que[2].text
        total_hard_questions = total_que[2].text

        total_problems_solved = soup.find('div', class_='text-[24px] font-medium text-label-1 dark:text-dark-label-1').text
        ranking = soup.find('span', class_='ttext-label-1').text

        result = {
            "username": self.__username, 
            "easy_questions_solved": easy_questions_solved,
            "total_easy_questions": total_easy_questions[1:],
            "medium_questions_solved": medium_questions_solved,
            "total_medium_questions": total_medium_questions[1:],
            "hard_questions_solved": hard_questions_solved,
            "total_hard_questions": total_hard_questions[1:],
            "total_problems_solved": total_problems_solved,
            "ranking": ranking,
        }
        
        return jsonify(result)

    def get_details(self):
        return self.get_detail()