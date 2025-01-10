# TODO(LOW): Create degreeworks scraper with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import json
from datetime import datetime
import time
# login
# filter for student info
# filter for all courses info

# Use webdriver waits for all operations


USERNAME = os.getenv("USERNAME") 
PASSWORD = os.getenv("PASSWORD")


class DegreeWorksScraper:
    def __init__(self, headless: bool = False):
        self.dashboard_url = "https://degreeworks.cuny.edu/Dashboard_bm" # direct link to BMCC degreeworks
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless")

        options.add_argument("--incognito")
        options.add_argument("--disable-info-bars")
        options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=options)

    def authenticate(self) -> bool:
        # FIXME: Need to clear the username field since it's populated with default values
        # input field > username id > CUNYfirstUsernameH 
        # input field > password id > CUNYfirstPassword
        self.driver.get(self.dashboard_url)
        username_element = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "CUNYfirstUsernameH")))
        
        username_element.clear()

        password_element = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "CUNYfirstPassword")))

        username_element.send_keys(USERNAME)
        password_element.send_keys(PASSWORD)

        log_in_btn = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "submit")))

        log_in_btn.send_keys(Keys.ENTER)
    
        # webdriver wait for successful login
    
        tofind = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Degree Audit')]")))
        return True

    def fetch_student_info(self):
        time.sleep(2)
        student_info = {}

        student_id_elem = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "student-id")))

        student_info["studentId"] = student_id_elem.get_attribute("value")
        print(student_id_elem.get_attribute("value"))

        # student-name
        student_name_elem = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "student-name")))

        student_info["name"] = student_name_elem.get_attribute("value")
        #degree
        student_degree_elem = WebDriverWait(
            self.driver, 30
        ).until(EC.presence_of_element_located((By.ID, "degree")))

        student_info["degree"] = student_degree_elem.get_attribute("value")

        expected_fields = {
            "Major": "major",  
            "Classification": "classification",  
            "Transfer Credits": "transferCredits",
            "Academic Status": "academicStatus"
        }

        # span tag > style = font-weight: bold; padding-right: 0.25rem;
        # child the span tag child then move up to the parent to get all the text
        # font-weight: bold; padding-right: 0.25rem;
        spans = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, 
                'div span[style*="font-weight: bold"][style*="padding-right: 0.25rem"], span[style*="font-weight: bold"][style*="padding-right: 0.25rem"]'
            ))
        )
        for span in spans:
            field_text = span.text
            parent_element = WebDriverWait(span, 10).until(
                EC.presence_of_element_located((
                    By.XPATH, 
                    "./.." 
                ))
            )

            full_text = parent_element.text

            if field_text in expected_fields:
                student_info[expected_fields[field_text]] = full_text[len(field_text) + 1:] # +1 to skip the blank space
            
        return student_info
    
    def fetch_course_info(self):
        pass

    def save_to_json(self, data: dict, filename: str = None) -> str:        #
        # Create an output directory if it doesn't exist
        output_dir = "degree_audits"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate default filename if none provided
        if filename is None:
            # Use student ID if available, otherwise use timestamp
            student_id = data.get("studentInfo", {}).get("studentId", "unknown")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"degree_audit_{student_id}_{timestamp}.json"
        
        # Ensure filename has .json extension
        if not filename.endswith('.json'):
            filename += '.json'
            
        filepath = os.path.join(output_dir, filename)
        
        # Add metadata to the export
        export_data = {
            "metadata": {
                "exportDate": datetime.now().isoformat(),
                "source": "DegreeWorks CUNY",
            },
            "data": data
        }
        
        # Write to JSON file with proper formatting
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
            
        return filepath    
    

def main():
    client = DegreeWorksScraper()
    audit_info = {}
    if client.authenticate():
        audit_info["studentInfo"] = client.fetch_student_info()
        json_path = client.save_to_json(audit_info)
        print(f"Audit information saved to: {json_path}")
    print(audit_info)



if __name__ == "__main__":
    main()