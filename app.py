from flask import *
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') 

services_info = {
    "tax-administration": """
        <ol>
            <li><strong>Taxpayer Registration and Compliance:</strong>
                <ul>
                    <li>Registered and onboarded new taxpayers, facilitated the filing of various tax returns such as Income Tax,VAT and Turnover Tax.</li>
                    <li>Verified tax returns and documents for accuracy, contacted taxpayers to ensure compliance.</li>
                </ul>
            </li>
            <li><strong>Tax Collection and Assessment:</strong>
                <ul>
                    <li>Assessed tax liabilities for individuals and businesses based on tax laws and income reports.</li>
                    <li>Collected taxes from various revenue streams, ensuring accurate reporting and remittance.</li>
                </ul>
            </li>
            <li><strong>Tax Audits and Investigations:</strong>
                <ul>
                    <li>Conducted routine and detailed audits to identify discrepancies in taxpayer declarations.</li>
                    <li>Investigated cases of tax evasion or fraud and recommended appropriate actions.</li>
                </ul>
            </li>
            <li><strong>Revenue Monitoring and Reporting:</strong>
                <ul>
                    <li>Monitored revenue collections and prepared periodic reports for senior management.</li>
                    <li>Ensured the implementation of systems for accurate tracking and reconciliation of revenue.</li>
                </ul>
            </li>
            <li><strong>Policy Interpretation and Advisory:</strong>
                <ul>
                    <li>Provided advice to taxpayers on tax regulations, incentives, and compliance requirements.</li>
                    <li>Interpreted tax laws and advised management on updates affecting operations.</li>
                </ul>
            </li>
            <li><strong>Tax Dispute Resolution:</strong>
                <ul>
                    <li>Managed disputes between taxpayers and the tax authority, ensuring fair and efficient resolution.</li>
                    <li>Represented the organization in arbitration or litigation proceedings.</li>
                </ul>
            </li>
            <li><strong>Stakeholder Engagement:</strong>
                <ul>
                    <li>Provided comprehensive training to new taxpayers on tax obligations and filing procedures.</li>
                    <li>Liaised with businesses, individuals, and government bodies to streamline tax-related processes.</li>
                </ul>
            </li>
            <li><strong>Use of Technology in Taxation:</strong>
                <ul>
                    <li>Utilized tax administration software to manage taxpayer records and automate processes.</li>
                    <li>Contributed to the digital transformation of tax operations, including e-filing systems.</li>
                </ul>
            </li>
            <li><strong>Data Analysis and Forecasting:</strong>
                <ul>
                    <li>Analyzed taxpayer data to identify trends and optimize revenue collection strategies.</li>
                    <li>Prepared forecasts to aid in policy development and budgeting.</li>
                </ul>
            </li>
            <li><strong>Compliance Enforcement:</strong>
                <ul>
                    <li>Issued notices and penalties for late payments or non-compliance with tax laws.</li>
                    <li>Ensured adherence to local, national, and international taxation standards.</li>
                </ul>
            </li>
            
        </ol>
    """,
    "network-administration": """
        <ol>
            <li><strong>Network Installation and Configuration:</strong>
                <ul>
                    <li>Designed, implemented, and maintained LAN, WAN, and wireless networks.</li>
                    <li>Configured network hardware, including routers, switches, firewalls, and servers.</li>
                </ul>
            </li>
            <li><strong>Troubleshooting and Maintenance:</strong>
                <ul>
                    <li>Diagnosed and resolved network performance issues to ensure minimal downtime.</li>
                    <li>Conducted routine maintenance to optimize network performance and reliability.</li>
                </ul>
            </li>
             <li><strong>Network Security:</strong>
                <ul>
                    <li>Implemented security protocols, firewalls, and VPNs to safeguard networks from unauthorized access and cyber threats.</li>
                    <li>Monitored networks for vulnerabilities and performed security updates.</li>
                </ul>
            </li>
            <li><strong>Backup Recovery</strong>
                <ul>
                    <li>Developed and maintained network backup recovery plans</li>
                </ul>
            </li>
            
        </ol>
    """,
    "data-analysis": """
        <ol>
            <li><strong>Data Collection and Management</strong>
                <ul>
                    <li>Gathered data from multiple sources, including databases, APIs, and spreadsheets.</li>
                    <li>Cleaned and structured raw data for analysis using tools like Python, Excel, and SQL.</li>
                </ul>
            </li>
            <li><strong>Data Visualization and Reporting:</strong>
                <ul>
                    <li>Created dashboards and visualizations using tools like Tableau, Power BI, and Matplotlib.</li>
                    <li>Presented actionable insights to stakeholders through detailed reports and presentations with pie charts, bar graphs and heatmaps.</li>
                </ul>
            </li>
             <li><strong>Statistical and Predictive Analysis</strong>
                <ul>
                    <li>Conducted hypothesis testing and regression analysis to derive insights.</li>
                    <li>Utilized Python libraries like Pandas, NumPy, and SciPy for data manipulation.</li>
                </ul>
            </li>
        </ol>
    """,
    "database-administration": """
        <ol>
            <li><strong>Database Design and Implementation</strong>
                <ul>
                    <li>Designed relational database schemas and ER models to meet organizational needs.</li>
                    <li>Installed and configured database management systems like MySQL, PostgreSQL, and Oracle.</li>
                </ul>
            </li>
            <li><strong>Database Maintenance:</strong>
                <ul>
                    <li>Performed regular backups, indexing, and optimization for efficient data retrieval.</li>
                    <li>Monitored database performance and resolved issues such as slow queries or storage limits.</li>
                </ul>
            </li>
            <li><strong>Security and Access Control:</strong>
                <ul>
                    <li>Implemented user access controls and encryption to secure sensitive data.</li>
                    <li>Conducted audits to ensure compliance with data protection regulations.</li>
                </ul>
            </li>
            <li><strong>Data Migration and Integration:</strong>
                <ul>
                    <li>Migrated data between systems while maintaining data integrity and minimizing downtime.</li>
                    <li>Integrated databases with external applications and APIs.</li>
                </ul>
            </li>
            <li><strong>Disaster Recovery:</strong>
                <ul>
                    <li>Developed recovery strategies to restore databases in case of failures or corruption.</li>
                    <li>Conducted regular recovery drills to ensure data restoration processes were effective.</li>
                </ul>
            </li>
            <li><strong>Documentation and Reporting:</strong>
                <ul>
                    <li>Maintained detailed documentation of database configurations, updates, and queries.</li>
                    <li>Generated reports for management on database performance and usage statistics.</li>
                </ul>
            </li>
        </ol>
    """,
    "web-development": """
        <ol>
            <li><strong>Website Design and Development:</strong>
                <ul>
                    <li>Developed responsive and user-friendly websites using HTML, CSS, JavaScript, and frameworks like Flask and Bootstrap.</li>
                    <li>Designed web interfaces that prioritize usability and accessibility.</li>
                </ul>
            </li>
            <li><strong>Back-End Development:</strong>
                <ul>
                    <li>Built and maintained server-side functionality using Flask and Python.</li>
                    <li>Connected websites to databases using MySQL or MongoDB to store and retrieve dynamic content.</li>
                </ul>
            </li>
            <li><strong>API Integration:</strong>
                <ul>
                    <li>Integrated third-party APIs for payment gateways, social media, and geolocation services.</li>
                    <li>Developed custom RESTful APIs to facilitate data exchange between systems.</li>
                </ul>
            </li>
            <li><strong>Security Implementation:</strong>
                <ul>
                    <li>Secured websites with HTTPS, secure authentication mechanisms, and input validation.</li>
                    <li>Conducted vulnerability assessments to identify and address security risks.</li>
                </ul>
            </li>
            <li><strong>Testing and Debugging:</strong>
                <ul>
                    <li>Performed end-to-end testing using tools like Selenium and unit testing frameworks.</li>
                    <li>Debugged and resolved errors to ensure seamless functionality across browsers.</li>
                </ul>
            </li>
            <li><strong>Deployment and Maintenance:</strong>
                <ul>
                    <li>Deployed websites on hosting platforms like AWS, Heroku, or local servers.</li>
                    <li>Provided post-launch support, updates, and troubleshooting services.</li>
                </ul>
            </li>
            <li><strong>Client Collaboration and Documentation:</strong>
                <ul>
                    <li>Worked closely with clients to understand requirements and provide tailored solutions.</li>
                    <li>Documented project workflows, updates, and user guides for long-term usability.</li>
                </ul>
            </li>
        </ol>
    """,
    "software-development": """
    <ol>
        <li><strong>Custom Software Development:</strong>
            <ul>
                <li>Designing and developing tailored software solutions to meet specific business needs.</li>
                <li>Creating desktop, web, and mobile applications with modern technologies.</li>
            </ul>
        </li>
        <li><strong>Full-Stack Web Development:</strong>
            <ul>
                <li>Building interactive and responsive websites using HTML, CSS, JavaScript, Flask, and Python.</li>
                <li>Developing backend systems with databases like MySQL for efficient data storage.</li>
            </ul>
        </li>
        <li><strong>API Development and Integration:</strong>
            <ul>
                <li>Developing RESTful APIs for seamless communication between different applications.</li>
                <li>Integrating third-party APIs such as payment gateways, social media, and cloud services.</li>
            </ul>
        </li>
        <li><strong>Software Testing and Quality Assurance:</strong>
            <ul>
                <li>Performing rigorous software testing to identify and fix bugs.</li>
                <li>Ensuring software applications meet security, performance, and usability standards.</li>
            </ul>
        </li>
        <li><strong>Database Management:</strong>
            <ul>
                <li>Designing and managing relational databases like MySQL to store and retrieve data efficiently.</li>
                <li>Optimizing database queries for high performance.</li>
            </ul>
        </li>
        <li><strong>Software Maintenance and Support:</strong>
            <ul>
                <li>Providing regular software updates and feature enhancements.</li>
                <li>Fixing bugs and improving system performance.</li>
            </ul>
        </li>
        <li><strong>Cloud Computing and Deployment:</strong>
            <ul>
                <li>Deploying applications on cloud platforms such as AWS, Google Cloud, or Digital Ocean.</li>
                <li>Ensuring high availability and scalability of applications.</li>
            </ul>
        </li>
        <li><strong>Cybersecurity Implementation:</strong>
            <ul>
                <li>Ensuring software applications are secure against threats like SQL injection and XSS.</li>
                <li>Implementing authentication, encryption, and secure data handling.</li>
            </ul>
        </li>
        <li><strong>Agile Software Development:</strong>
            <ul>
                <li>Following agile methodologies for iterative development and continuous improvements.</li>
                <li>Working closely with clients to ensure project goals are met efficiently.</li>
            </ul>
        </li>
    </ol>
"""

}


@app.route('/')
def home():
    return render_template('index.html' , services=services_info)

@app.route("/service/<service_name>")
def service(service_name):
    
    service_detail = services_info.get(service_name, "<p>Details not available for this service.</p>")
    return render_template("service_detail.html", service_detail=service_detail)

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')



app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject', 'No Subject')  
    message_body = request.form.get('message')

    
    if not name or not email or not message_body:
        flash("Name, email, and message are required!", "danger")
        return redirect('/#contact')

    # Create Email Message
    msg = Message(
        subject=f"Portfolio Contact Form Submission: {subject}",
        sender=email,
        recipients=["boazmittoh480@gmail.com"],
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
    )

    try:
        mail.send(msg)
        flash("Your message has been sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending message: {str(e)}", "danger")

    return redirect('/#contact')



if __name__ == '__main__':
    app.run(debug=True, port=4000)
