from functions import company_reader,grabs_page,all_url_links,facebook_link,get_facebook_page, pick_phonenumber,formatting,result_panel
 

companies=company_reader("file.txt")

for company in companies:

    response = grabs_page(company)
    
    all_links = all_url_links(response)
    
    link = facebook_link(all_links)
    
    facebook_content = get_facebook_page(link)
    
    phonenumber = pick_phonenumber(facebook_content)
    
    stripped_number = formatting(phonenumber)
    
    result = result_panel(company,stripped_number)
    print(result)
    