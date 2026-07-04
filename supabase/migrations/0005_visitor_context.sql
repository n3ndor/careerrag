-- Coarse visitor context per question: country/city (from Vercel's edge geo
-- headers) and device family (from the user agent). No raw IPs, no
-- fingerprinting; just enough to know where interest comes from.

alter table careerrag_questions
    add column country text,
    add column city text,
    add column device text;
