from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="Your-Key-Here")

business_context = """
You are a friendly customer service assistant for Hands4YouAssembly, 
a professional assembly service based in the Maryland/DMV area.
Services: IKEA furniture, office furniture, gym equipment, TV mounting.
Service area: Maryland, DC, and Northern Virginia.
For quotes contact: 301-537-8884 or brandaneisbey@gmail.com
Pricing varies by job — direct customers to call or email for a free quote.
Always be friendly and professional.
"""

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/hub")
def hub():
    return render_template("hub.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": business_context},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)
