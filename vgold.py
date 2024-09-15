import streamlit as st

# Function to display navigation
def show_nav():
    menu = ['Home', 'Products', 'About Us', 'Contact Us']
    choice = st.sidebar.selectbox('Menu', menu)
    return choice

# Function to display homepage
def show_home():
    st.title('Welcome to VGold Grocery Store')
    st.write('Find fresh groceries at affordable prices!')

# Function to display products page
def show_products():
    st.title('Our Products')
    products = [f"Item {i}" for i in range(1, 34)]  # 33 products
    for product in products:
        st.write(f"- {product}")

# Function to display About Us page
def show_about():
    st.title('About Us')
    st.write('VGold is your trusted online grocery store offering fresh, organic, and affordable groceries.')

# Function to display Contact Us page
def show_contact():
    st.title('Contact Us')
    st.write('Email: contact@vgold.com')
    st.write('Phone: +123 456 7890')
    st.write('Address: 123 Grocery Lane, Market City')

# Main function
def main():
    st.sidebar.title("VGold Navigation")
    choice = show_nav()

    if choice == 'Home':
        show_home()
    elif choice == 'Products':
        show_products()
    elif choice == 'About Us':
        show_about()
    elif choice == 'Contact Us':
        show_contact()

if __name__ == '__main__':
    main()
