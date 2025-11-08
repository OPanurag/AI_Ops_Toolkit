# 📞 AutoDialer – AI-Powered Voice Call Automation System

### Overview

**AutoDialer** is an experimental project built with **Ruby on Rails**, designed to trigger automated outbound phone calls via command-line or web interface.
The system allows a user to issue simple text commands like:

```bash
call +919812345678
```

Upon execution, the backend initiates an automated outbound voice call using a pre-defined or dynamically generated script. The voice message can either be:

1. **Static script** – Predefined message (e.g., appointment reminder or sales pitch).
2. **Dynamic AI-generated script** – Created on-the-fly using an AI model (like OpenAI GPT or Google Gemini) based on context or user input.

---

## ⚙️ System Architecture

### 1. Frontend (Command or Web UI)

* Minimal **Rails-based interface** where a user enters a phone number and message type.
* Input accepted via:

  * Terminal command (`call +91XXXXXXXXXX`) or
  * Web form with fields: *Phone Number* and *Message Template/Type*.

### 2. Backend (Ruby on Rails API Layer)

* Core logic built in **Ruby on Rails**.
* When a call command is received:

  * It invokes a controller endpoint like `/api/v1/autodialer/call`.
  * Validates phone number format (E.164 format, e.g., +919812345678).
  * Retrieves or generates a message script (via AI API or static templates).

### 3. Telephony Integration Layer

* Uses **Twilio Voice API** (or Plivo / Vonage) for actual call initiation.
* Typical workflow:

  1. Send an API request to Twilio with destination number and TwiML (Twilio Markup Language) payload.
  2. Twilio servers initiate the outbound call and stream the voice (either text-to-speech or pre-recorded audio).
  3. Logs the call status (success, failed, not answered, etc.) back to the Rails app.

Example call initiation pseudocode:

```ruby
@client = Twilio::REST::Client.new(ENV['TWILIO_SID'], ENV['TWILIO_AUTH_TOKEN'])
call = @client.calls.create(
  to: "+919812345678",
  from: "+12015551234",
  twiml: "<Response><Say>Hi! This is an automated message from your AI dialer.</Say></Response>"
)
```

### 4. AI Voice Script Generator (Optional)

If dynamic voice messages are enabled:

* The app calls the AI API (e.g., Gemini or GPT) with a context prompt such as:

  ```
  "Generate a friendly and professional 20-second message for confirming an appointment with Mr. Sharma."
  ```
* The returned text is then sent to Twilio’s **Text-to-Speech (TTS)** for real-time conversion to voice.

---

## 🗂️ Folder Structure

```
autodialer/
│
├── app/
│   ├── controllers/
│   │   └── autodialer_controller.rb
│   ├── views/
│   │   └── autodialer/
│   │       └── index.html.erb
│   └── models/
│
├── config/
│   ├── routes.rb
│   └── initializers/
│       └── twilio.rb
│
├── lib/
│   └── ai_script_generator.rb
│
├── db/
│   └── schema.rb
│
├── .env (contains TWILIO_SID, TWILIO_AUTH_TOKEN, AI_API_KEY)
└── README.md
```

---

## 🔧 Environment Variables

```
TWILIO_SID=<your_twilio_account_sid>
TWILIO_AUTH_TOKEN=<your_twilio_auth_token>
TWILIO_PHONE_NUMBER=<your_twilio_registered_number>
AI_API_KEY=<your_gemini_or_openai_key>
```

---

## 🧠 Typical Flow

1. User enters `call +91XXXXXXXXXX` or uses the frontend.
2. Rails validates input → generates AI text → sends TwiML payload to Twilio.
3. Twilio dials the number and reads the message via TTS.
4. Rails app logs the status and displays “Call initiated successfully.”

---

## 🚫 Legal & Operational Limitations

### 1. **Telecom Regulatory Authority of India (TRAI) Restrictions**

Under **TRAI and DoT (Department of Telecommunications)** regulations:

* Automated outbound calls (robocalls) are strictly controlled.
* Only **registered telemarketers with approved Sender IDs and use-cases** can initiate bulk or automated voice calls.
* Use of **foreign VoIP gateways (e.g., Twilio US-based)** to route calls into Indian mobile numbers is **prohibited without explicit licensing**.

### 2. **International Number Routing Issues**

* Twilio (or similar providers) often assign **U.S. or European numbers**.
* When these are used to call Indian numbers, the call incurs **international call rates** (high per-minute cost).
* In most cases, the calls will be **blocked or flagged as spam/invalid** by Indian carriers due to anti-spoofing measures.

### 3. **Data Privacy Compliance**

* Recording or storing voice call data without user consent violates **India’s Personal Data Protection (PDP) framework**.
* AI-generated voice messages that impersonate a human (even partially) may breach **consent and misrepresentation clauses**.

### 4. **Testing Constraints**

* Developers cannot use Twilio’s sandbox for real calls to India due to **geo restrictions**.
* Buying a USA-based number incurs cost and only works for **calls within U.S. or approved destinations**.
* Hence, even small-scale testing (like “hello world” calls) results in **international call charges** and **possible number blocking**.

---

## 🧩 Conclusion

While **AutoDialer** is a technically viable and elegant demonstration of AI–Telephony integration, it is **not deployable in production** within India without:

1. A licensed telemarketing registration under **TRAI’s Distributed Ledger Technology (DLT)** framework.
2. Approval for use of **domestic telephony gateways** (e.g., Exotel, Knowlarity, MyOperator, or Tata Tele).
3. Compliance with **call consent and data retention regulations**.

For R&D, the logic can still be tested locally or simulated using **Twilio’s Voice Simulator** or **local mock endpoints**, but **real number dialing** to Indian users remains legally and economically impractical.

---

## 🧑‍💻 Author

**Anurag Mishra**
AI & ML Engineer | Data Scientist
📧 [officiallyanurag1@gmail.com](mailto:officiallyanurag1@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/anuragmishra02/)
💻 [GitHub](https://github.com/OPanurag)

---

## ⚖️ Disclaimer

This project is for **educational and research purposes only**.
Scraping LinkedIn or other platforms without permission may violate their Terms of Service.
Use responsibly.