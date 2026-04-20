import Anthropic from '@anthropic-ai/sdk';

const ALLOWED_ORIGIN = 'https://inmagent.com';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', ALLOWED_ORIGIN);
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { images, notes } = req.body || {};

  const client = new Anthropic();

  const content = [];

  if (images && images.length > 0) {
    images.forEach(img => {
      content.push({
        type: 'image',
        source: { type: 'base64', media_type: img.mediaType || 'image/jpeg', data: img.base64 }
      });
    });
  }

  content.push({
    type: 'text',
    text: `You are helping Jake at INMA (Inland Northwest Marketing Affiliates, Spokane WA) build a project estimate from job site photos and notes.

SCOPE NOTES FROM JAKE:
${notes || '(no notes provided)'}

Based on the photos and notes, estimate quantities for this project. Use these FMV pricing defaults:

SIDING:
- Primed Hardie B&B: $12.50/SF
- ColorPlus Hardie: $19.00/SF
- Aluminum Soffit: $13.00/LF
- Aluminum Fascia: $8.50/LF
- Post/Beam Wrap: $12.00/LF
- Tearoff/Dump/Cleanup: $1.50/SF (match total siding SF)

WINDOWS (per unit):
- Small (≤20 SF): $425/ea
- Medium (21–40 SF): $900/ea
- Large (>40 SF): $1,200/ea

TRIM:
- Interior Trim: $4.00/LF
- Exterior Trim/Belly Band: $5.00/LF

Estimate conservatively — Jake will adjust. If you cannot determine a quantity, use 0.

Respond ONLY with valid JSON, no other text:

{
  "siding": {
    "primed_hardie_qty": 0, "primed_hardie_rate": 12.50,
    "colorplus_qty": 0, "colorplus_rate": 19.00,
    "soffit_qty": 0, "soffit_rate": 13.00,
    "fascia_qty": 0, "fascia_rate": 8.50,
    "wrap_qty": 0, "wrap_rate": 12.00,
    "tearoff_qty": 0, "tearoff_rate": 1.50
  },
  "windows": {
    "small_qty": 0, "small_rate": 425,
    "medium_qty": 0, "medium_rate": 900,
    "large_qty": 0, "large_rate": 1200
  },
  "trim": {
    "interior_qty": 0, "interior_rate": 4.00,
    "exterior_qty": 0, "exterior_rate": 5.00
  },
  "ai_notes": "Brief summary of what you observed and estimated"
}`
  });

  const message = await client.messages.create({
    model: 'claude-haiku-4-5-20251001',
    max_tokens: 1000,
    messages: [{ role: 'user', content }]
  });

  const text = message.content[0].text;

  try {
    return res.status(200).json({ estimate: JSON.parse(text) });
  } catch(e) {
    const match = text.match(/\{[\s\S]*\}/);
    if (match) {
      try { return res.status(200).json({ estimate: JSON.parse(match[0]) }); } catch(e2) {}
    }
    return res.status(200).json({ estimate: null, raw: text });
  }
}
