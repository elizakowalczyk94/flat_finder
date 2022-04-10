from bs4 import BeautifulSoup
import requests
import time

CHECK_IN = "2022/04/30"
CHECK_OUT = "2022/05/05"
checkin_y, checkin_m, checkin_d = CHECK_IN.split("/")
checkout_y, checkout_m, checkout_d = CHECK_OUT.split("/")
BOOKING_URL = f"https://www.booking.com/searchresults.en-gb.html?label=apartments-tuKZpYPj11PgkeFBnHUNSgS228625778595%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-2294637490%3Alp1011325%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg&sid=e3ddd48cb4140e5c63c9a968046d2892&aid=309654&src=searchresults&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D309654%26label%3Dapartments-tuKZpYPj11PgkeFBnHUNSgS228625778595%253Apl%253Ata%253Ap1%253Ap2%253Aac%253Aap%253Aneg%253Afi%253Atikwd-2294637490%253Alp1011325%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg%26sid%3De3ddd48cb4140e5c63c9a968046d2892%26tmpl%3Dsearchresults%26ac_click_type%3Db%3Bac_position%3D0%3Bclass_interval%3D1%3Bdest_id%3D20015732%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Biata%3DSFO%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bsearch_selected%3D1%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dindex%3Bsrc_elem%3Dsb%3Bsrpvid%3Dd88f693358300227%3Bss%3DSan%2520Francisco%252C%2520California%252C%2520United%2520States%3Bss_all%3D0%3Bss_raw%3Dsan%2520francisco%3Bssb%3Dempty%3Bsshis%3D0%3Btheme_id%3D1%3Btheme_source%3Dindex%26%26&ss=San+Francisco&is_ski_area=0&ssne=San+Francisco&ssne_untouched=San+Francisco&city=20015732&checkin_year={checkin_y}&checkin_month={checkin_m}&checkin_monthday={checkin_d}&checkout_year={checkout_y}&checkout_month={checkout_m}&checkout_monthday={checkout_d}&group_adults=2&group_children=0&no_rooms=1&from_sf=1&sr_change_search=2&nflt=pri%3D5"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

response = requests.get(BOOKING_URL, headers=HEADERS)
booking_webpage = response.text

soup = BeautifulSoup(booking_webpage, "lxml")
time.sleep(1)
apartments = soup.find_all(name="div", attrs={"data-testid": "property-card"})
apartments_data = []
for ap in apartments:
    ap_data = {}
    ap_url = ap.find("a")
    ap_data["url"] = ap_url.get("href")
    ap_data["name"] = ap_url.getText()
    price = ap.find("span", class_="fcab3ed991 bd73d13072")
    ap_data["price"] = price.text.split()[0].replace(",", "")
    apartments_data.append(ap_data)

print(apartments_data)
time.sleep(2)
