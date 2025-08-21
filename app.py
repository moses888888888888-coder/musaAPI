from flask import Flask, render_template, send_file
import io
from fpdf import FPDF
import scheduler  # Ensure this module exists and includes the required functions and constants

app = Flask(__name__)

@app.route('/')
def home():
    timetable = scheduler.generate_timetable_data()
    return render_template('home.html', timetable=timetable, lesson_times=scheduler.LESSON_TIMES)

@app.route('/download-pdf')
def download_pdf():
    timetable = scheduler.generate_timetable_data()

    # Example PDF generation (you can customize layout/style)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for grade, days in timetable.items():
        pdf.cell(200, 10, txt=f"Grade: {grade}", ln=True)
        for day, subjects in days.items():
            pdf.cell(200, 10, txt=f"  {day}: {', '.join(subjects)}", ln=True)
        pdf.ln(5)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, download_name="timetable.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Render!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Timetable API is live!"


