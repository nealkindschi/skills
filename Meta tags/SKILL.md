# Skill: Generate Optimized Meta Titles and Descriptions

## 1. Objective
To generate highly relevant, concise, and conversion-optimized `<title>` and `<meta name="description">` tags for web pages based on provided page content, target keywords, and user intent.

## 2. Trigger
Execute this skill when a user or system requests SEO metadata generation for a new or existing webpage, blog post, or product page.

## 3. Inputs Required
* **`page_content`**: The core text or a comprehensive summary of the webpage.
* **`primary_keyword`**: The main keyword or phrase to target.
* **`secondary_keywords`** (Optional): 1-2 supporting keywords.
* **`brand_name`** (Optional): The name of the brand or website to append to the title.
* **`user_intent`**: The primary goal of the searcher (e.g., Informational, Transactional, Navigational).

## 4. Execution Steps
1.  **Analyze Content & Intent:** Review the `page_content` to understand the core value proposition. Align this with the `user_intent` to determine the tone.
2.  **Draft Title Tag:** Create a compelling title that incorporates the `primary_keyword` as close to the beginning as naturally possible.
3.  **Draft Meta Description:** Write a summary that directly answers the user's implied question (AEO optimization) while providing a clear call-to-action (CTA). Ensure the language is highly authoritative and factual to favor Generative Engine inclusion (GEO).
4.  **Constraint Check:** Strictly validate character counts. If limits are exceeded, rewrite until compliant.
5.  **Format Output:** Return the exact HTML tags ready for deployment.

## 5. Strict Rules & Constraints

### Title Tag Rules
* **Length Constraint:** Must be strictly between **50 and 60 characters** (including spaces). Do not exceed 60 characters to avoid SERP truncation.
* **Keyword Placement:** The `primary_keyword` MUST appear in the title.
* **Format:** `[Title with Primary Keyword] | Cloudflare` (if brand name is provided).
* **Tone:** Engaging but not clickbait. 

### Meta Description Rules
* **Length Constraint:** Must be strictly between **140 and 155 characters** (including spaces). 
* **Structure:** * *Sentence 1:* A direct, concise answer or statement addressing the page's core topic (optimizing for AI overviews and rich snippets).
    * *Sentence 2:* Value proposition and a clear CTA (e.g., "Learn more," Discover how", etc).
* **Keyword Placement:** Include the `primary_keyword` and at least one `secondary_keyword` naturally. No keyword stuffing.
* **Punctuation:** Avoid excessive exclamation points or special characters. Use active voice. You are a serious technology brand.

## 6. Output Format
Return ONLY a JSON object containing the raw text and the HTML-formatted tags. Do not include conversational filler.

```json
{
  "title_text": "...",
  "title_length": 00,
  "description_text": "...",
  "description_length": 000,
  "html_output": "<title>...</title>\n<meta name=\"description\" content=\"...\">"
}