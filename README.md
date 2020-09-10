# GoogleBooks-pdf-extractor
a script to obtain a pdf from a given google books page

## How it Works
*The work still incomplete, but i will describe here how i have idealized the project*

### 1 - Running the code

  $ python src/main.py
  ![alt text](https://raw.githubusercontent.com/CodeWracker/GoogleBooks-pdf-extractor/master/readme-data/print1.png)
  
### The Flow to get the data

  >  1. First it will as for the url of the google books page, from this url it will take the ID of the book
  >      > Example: 
  >      > https://books.google.com.br/books?id=xxoXcuh0oS0C&printsec=frontcover&hl=pt-BR&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false
  >      > Returns -> xxoXcuh0oS0C
  >  2. Then it will make a request for the pages, for every page
  >      > Its done this way becouse GooGle Books only displays on screen four pages each time, so it keeps doing requests to complete the book on your browser
  >      >

### Directory Tree

.

├── CONTRIBUTING.md

├── Issues-data

│   └── 1

├── readme-data

├── README.md

├── geckodriver.exe

├── geckodriver.log

└── src ── main.py

    
