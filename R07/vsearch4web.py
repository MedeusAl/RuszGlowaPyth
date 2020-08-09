
from flask import Flask, render_template, request
from  defFunction import search4letters
from _datetime import datetime
from flask import escape

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
   phrase = request.form['phrase']
   letters = request.form['letters']
   title = 'Oto Twoje wyniki:'
   results = str(search4letters(phrase, letters))
   log_request(request, results)
   return render_template('results.html',
                          the_title=title,
                          the_phrase=phrase,
                          the_letters=letters,
                          the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
   return render_template('entry.html',
                          the_title='Witamy na stronie internetowej search4letters!')
@app.route('/viewlog')
def view_the_log() -> 'html':
    '''output jest w formie linii ciaglej bez enterow. slabo czytelny'''
    # with open('vsearch.log') as log:
    #     contents = log.readlines()
    # return escape(''.join(contents))
    '''zmieniony kod metody view_log w celu wrzucenia na liste logow'''
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('dane z formularza', 'adres klienta', 'agent uzytkownika', 'wyniki')
    return render_template('viewlog.html',
                            the_title='Logi',
                            the_row_titles=titles,
                            the_data=contents,)

def log_request (req: 'flask_request', res: str) -> None :
    with open ('vsearch.log', 'a') as log:
        #print(datetime.today(), str(dir(req)) + str(res), file=log) #różnica zapisu req, res VS str(req) + str(res) !logi zapisuja sie dobrze
        # print(req.form, req.remote_addr, req.user_agent, res, file=log)
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log)

if __name__ == '__main__':
   app.run(debug=True)
