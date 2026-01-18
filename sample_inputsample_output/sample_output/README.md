# DocVision-AI-Convolve-R2

An end-to-end Document AI system for extracting structured information from scanned invoices and PDFs.

## What it does
- Takes PDF or image invoices as input  
- Performs OCR + Layout Understanding  
- Extracts key fields (Dealer Name, Model, HP, Cost, Signature, Stamp)  
- Validates data using rules + LLM reasoning  
- Outputs clean, structured JSON with confidence scores  

## Pipeline
1. Document Ingestion  
2. OCR & Visual Understanding  
3. Layout-Aware Parsing  
4. Field Detection & Reasoning  
5. Post-Processing & Validation  
6. JSON Output Generation  

## Sample Outputs
All example JSON outputs for real invoice pages are available in:
