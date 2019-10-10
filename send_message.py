
@author: daniel.lopez
"""

# =============================================================================
# Load libraries
# =============================================================================
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# =============================================================================
# Open web browser
# =============================================================================

# Install the driver if you don't have already have it
driver = webdriver.Chrome(ChromeDriverManager().install())

# Call the whatsapp webpage
driver.get('https://web.whatsapp.com/')

# Put the name of the people/groups you want to send it to
envios = ['contact','group']

"""
Remember that all the conversations must be opened manually. This will 
only send the message to people who's conversation is opened
"""

# =============================================================================
# Prepare the message
# =============================================================================

#name = input('Enter name of user or group to send message:')
msg = input('Enter your message:' )
count = int(input('Enter the number of messages to send:'))

input('Enter anything after scanning QR code' )

for name in envios:

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
