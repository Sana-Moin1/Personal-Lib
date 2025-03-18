import streamlit as st
import json

# load and save library data

def load_library():
    try:
        with open('library.json', 'r') as file:
            return  json.load(file)
    except FileNotFoundError:   
        return []
    
def save_library():
    with open('library.json', 'w') as file:
        json.dump(library, file, indent=4)

        # initialize library
library = load_library()

st.title('Personal Library App')
menu= st.sidebar.radio('Select  an option', ['View Library', 'Add a Book', 'Delete a Book', 'Search Book', 'Save and Quit'])
if menu == 'View Library':
    st.sidebar.write("Your Library")
    if library:
        st.table(library)
    else:
        st.write('No book in your library. Add some books!!')

#Add book
elif menu == "Add a Book":
    st.sidebar.write("Add a new Book")
    title = st.text_input('Title')
    author = st.text_input('Author')
    year = st.number_input('Year', min_value=2022, max_value=2100, step=1)
    genre = st.text_input('Genre')
    read_status = st.checkbox('Mark as Read')

    if st.button('Add Book'):
            library.append({'title': title, 'author': author, 'year': year, 'genre': genre, 'read_status': read_status})
            save_library()
            st.success('Book added successfully')
            st.rerun()     
    
    # Delete book
elif menu == 'Delete a Book':
    st.sidebar.write("Delete a Book")
    book_titles = [book['title'] for book in library]
    
    if book_titles:
        selected_book = st.selectbox('Select a book to delete', book_titles)
        if st.button('Delete Book'):
            library = [book for book in library if book['title'] != selected_book]
            save_library()
            st.success('Book deleted successfully')
            st.rerun()
    else:    
        st.warning('No book in your library. Add some books!!')
    
    # Search 
elif menu == 'Search Book':
    st.sidebar.write("Search Book")
    search_term = st.text_input('Enter a title or author name')    

    if st.button('Search'):
        results = [book for book in library if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        if results:
            st.table(results)
        else:
            st.warning('No book found')
    
    # Save and Quit
elif menu == 'Save and Quit':
    save_library()
    st.success('Library saved sucessfully. See you soon!')
    st.balloons()