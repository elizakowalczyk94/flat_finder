import time
from form_fill import FormFill
from booking_search import BookingSearch

CHECK_IN = "2022/04/30"
CHECK_OUT = "2022/05/05"

booking_finder = BookingSearch(check_in=CHECK_IN, check_out=CHECK_OUT)
booking_apartments = booking_finder.find_apartments()
print(booking_apartments)

form_filler = FormFill()
# form_filler.login() # Can't login because of Google security system.
form_filler.fill_google_form(booking_apartments)
# form_filler.create_spreadsheet() # Can't generate spreadsheet with form answers, because user not logged in.
time.sleep(5)
form_filler.quit_chrome()
