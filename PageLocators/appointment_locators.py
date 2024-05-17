class appointmentLocators:
    MOUSEHOVER_MANAGEMENT_XPATH = "//a[normalize-space()='Management']"
    SECTION_SELECTION_XPATH = "//a[@href='categories']//span[contains(text(),'Sections')]"
    CHOOSE_PERSONAL_XPATH = "//div[@class='row']//a[1]"
    SELECT_PREPARATION_DATE_XPATH ="//span[contains(text(),'اعداد ومواعيد')]"
    SPECIAL_APPOINTMENT_XPATH ="//button[@class='btn btn-info']"

    EXPRESS_SHIPPING_NAME = "shipping_method_ids[]"
    DELIVERY_PRICE_NAME = "delivery"
    FROM_TIME_XPATH = "//input[@name='delivery_times[times][0][from]']"
    TO_TIME_XPATH = "//input[@name='delivery_times[times][0][to]']"


