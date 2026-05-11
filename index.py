# =========================================================
# PROFESSIONAL CGPA & GPA CALCULATOR WITH FRONTEND
# =========================================================

from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Professional CGPA Calculator</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    min-height:100vh;
    padding:40px;
    color:white;
}

.container{
    max-width:1200px;
    margin:auto;
}

.header{
    text-align:center;
    margin-bottom:40px;
}

.header h1{
    font-size:50px;
    color:#38bdf8;
    margin-bottom:10px;
}

.header p{
    color:#cbd5e1;
    font-size:18px;
}

.dashboard{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:25px;
}

.semester-card{
    background:#1e293b;
    padding:25px;
    border-radius:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.3);
}

.semester-card h2{
    color:#38bdf8;
    margin-bottom:20px;
}

.input-group{
    margin-bottom:18px;
}

label{
    display:block;
    margin-bottom:8px;
    color:#cbd5e1;
}

input{
    width:100%;
    padding:14px;
    border:none;
    border-radius:12px;
    background:#334155;
    color:white;
    font-size:16px;
}

button{
    width:100%;
    margin-top:30px;
    padding:18px;
    border:none;
    border-radius:15px;
    background:#38bdf8;
    color:white;
    font-size:22px;
    cursor:pointer;
}

button:hover{
    background:#0ea5e9;
}

.summary{
    margin-top:40px;
    background:#1e293b;
    padding:35px;
    border-radius:20px;
}

.summary h2{
    text-align:center;
    margin-bottom:30px;
    color:#38bdf8;
}

.summary-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
}

.box{
    background:#334155;
    padding:25px;
    border-radius:18px;
    text-align:center;
}

.box h3{
    color:#cbd5e1;
    margin-bottom:15px;
}

.box p{
    font-size:35px;
    color:#22c55e;
    font-weight:bold;
}

.grade{
    text-align:center;
    margin-top:30px;
}

.grade h1{
    font-size:70px;
    color:#facc15;
}

.status{
    margin-top:10px;
    font-size:22px;
    color:#22c55e;
}

.footer{
    text-align:center;
    margin-top:40px;
    color:#94a3b8;
}

table{
    width:100%;
    margin-top:35px;
    border-collapse:collapse;
    overflow:hidden;
    border-radius:15px;
}

th{
    background:#38bdf8;
    padding:16px;
}

td{
    background:#334155;
    padding:16px;
    text-align:center;
    border-bottom:1px solid rgba(255,255,255,0.1);
}

</style>

</head>

<body>

<div class="container">

    <div class="header">

        <h1>🎓 CGPA & GPA Calculator</h1>

        <p>Professional Academic Analytics Dashboard</p>

    </div>

    <form method="POST">

    <div class="dashboard">

        {% for i in range(1,9) %}

        <div class="semester-card">

            <h2>Semester {{i}}</h2>

            <div class="input-group">

                <label>Enter GPA</label>

                <input type="number"
                step="0.01"
                name="sem{{i}}"
                placeholder="Example: 8.5"
                required>

            </div>

        </div>

        {% endfor %}

    </div>

    <button type="submit">
        Calculate Performance
    </button>

    </form>

    {% if cgpa %}

    <div class="summary">

        <h2>📊 Performance Summary</h2>

        <div class="summary-grid">

            <div class="box">

                <h3>Total GPA</h3>

                <p>{{total}}</p>

            </div>

            <div class="box">

                <h3>CGPA</h3>

                <p>{{cgpa}}</p>

            </div>

            <div class="box">

                <h3>Percentage</h3>

                <p>{{percentage}}%</p>

            </div>

        </div>

        <div class="grade">

            <h1>{{grade}}</h1>

            <div class="status">

                {{performance}}

            </div>

        </div>

        <table>

            <tr>
                <th>Semester</th>
                <th>GPA</th>
                <th>Status</th>
            </tr>

            {% for sem in semester_data %}

            <tr>

                <td>{{sem.sem}}</td>

                <td>{{sem.gpa}}</td>

                <td>{{sem.status}}</td>

            </tr>

            {% endfor %}

        </table>

    </div>

    {% endif %}

    <div class="footer">

        Professional CGPA Calculator • Flask + Python

    </div>

</div>

</body>

</html>

"""

@app.route("/", methods=["GET","POST"])

def home():

    if request.method == "POST":

        gpas = []

        semester_data = []

        for i in range(1,9):

            gpa = float(request.form[f"sem{i}"])

            gpas.append(gpa)

            if gpa >= 9:
                status = "Outstanding"

            elif gpa >= 8:
                status = "Excellent"

            elif gpa >= 7:
                status = "Very Good"

            elif gpa >= 6:
                status = "Good"

            else:
                status = "Average"

            semester_data.append({
                "sem":f"Semester {i}",
                "gpa":gpa,
                "status":status
            })

        total = round(sum(gpas),2)

        cgpa = round(total / len(gpas),2)

        percentage = round(cgpa * 9.5,2)

        if cgpa >= 9:

            grade = "O"
            performance = "Outstanding Performance"

        elif cgpa >= 8:

            grade = "A+"
            performance = "Excellent Performance"

        elif cgpa >= 7:

            grade = "A"
            performance = "Very Good Performance"

        elif cgpa >= 6:

            grade = "B"
            performance = "Good Performance"

        else:

            grade = "C"
            performance = "Needs Improvement"

        return render_template_string(

            HTML,

            total=total,
            cgpa=cgpa,
            percentage=percentage,
            grade=grade,
            performance=performance,
            semester_data=semester_data

        )

    return render_template_string(HTML)

if __name__ == "__main__":

    app.run(debug=True)