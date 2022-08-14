from tkinter import *
import be

def reset_entries():
  e_title.delete(0,END)
  e_author.delete(0,END)
  e_year.delete(0,END)
  e_isbn.delete(0,END)

def get_selected_item(event):
  try:
    global selected_tuple
    index=list_result.curselection()[0]
    selected_tuple=list_result.get(index)
    reset_entries()
    e_title.insert(END,selected_tuple[1])
    e_author.insert(END,selected_tuple[2])
    e_year.insert(END,selected_tuple[3])
    e_isbn.insert(END,selected_tuple[4])
  except IndexError:
    pass

window=Tk()
window.wm_title("Book store")

l_title=Label(window, text="Title")
l_title.grid(row=0,column=0)
l_author=Label(window, text="Author")
l_author.grid(row=0,column=2)
l_year=Label(window, text="Year")
l_year.grid(row=1,column=0)
l_isbn=Label(window, text="ISBN")
l_isbn.grid(row=1,column=2)

title_text=StringVar()
e_title=Entry(window, textvariable=title_text)
e_title.grid(row=0,column=1)

author_text=StringVar()
e_author=Entry(window, textvariable=author_text)
e_author.grid(row=0,column=3)

year_text=StringVar()
e_year=Entry(window, textvariable=year_text)
e_year.grid(row=1,column=1)

isbn_text=StringVar()
e_isbn=Entry(window, textvariable=isbn_text)
e_isbn.grid(row=1,column=3)

list_result=Listbox(window, height=6, width=35)
list_result.grid(row=2,column=0,rowspan=6,columnspan=2)

scrbar=Scrollbar(window)
scrbar.grid(row=2,column=2,rowspan=6)

list_result.configure(yscrollcommand=scrbar.set)
scrbar.configure(command=list_result.yview)

list_result.bind('<<ListboxSelect>>',get_selected_item)

"""
Commands
"""
def list_reset():
  list_result.delete(0,END)
def list_append(item):
  list_result.insert(END,item)

def view_all_command():
  rows=be.view()
  list_reset()
  for row in rows:
    list_append(row)

def search_command():
  list_reset()
  res=be.search(
    title=title_text.get(),
    author=author_text.get(),
    year=year_text.get(),
    isbn=isbn_text.get()
  )
  for row in res:
    list_append(row)

def add_command():
  be.insert(
    title=title_text.get(),
    author=author_text.get(),
    year=year_text.get(),
    isbn=isbn_text.get()
  )
  view_all_command()

def delete_command():
  be.delete(str(selected_tuple[0]))
  view_all_command()

def update_command():
  be.update(
    str(selected_tuple[0]),
    title_text.get(),
    author_text.get(),
    year_text.get(),
    isbn_text.get()
  )
  view_all_command()

"""
Buttons
"""
b_viewall=Button(window, text="View all", width=12,command=view_all_command)
b_viewall.grid(row=2,column=3)

b_search=Button(window, text="Search", width=12,command=search_command)
b_search.grid(row=3,column=3)

b_add=Button(window, text="Add", width=12,command=add_command)
b_add.grid(row=4,column=3)

b_update=Button(window, text="Update", width=12, command=update_command)
b_update.grid(row=5,column=3)

b_delete=Button(window, text="Delete", width=12,command=delete_command)
b_delete.grid(row=6,column=3)

b_close=Button(window, text="Close", width=12, command=window.destroy)
b_close.grid(row=7,column=3)

window.mainloop()