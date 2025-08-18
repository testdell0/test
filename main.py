from flask import Flask, request, jsonify
from PyPDF2 import PdfMerger, PdfReader
import os
import time
import gc

app = Flask(__name__)

@app.route('/home')
def home():
    return "RUNNING!!!"

@app.route('/merge', methods=['GET'])
def merge():
    emp = request.args.get('emp')
    directory_path = r'E:\Uploads\PDFMerge'
    
    try:
        pdfs = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)) and f.lower().endswith('.pdf') and emp in f.lower()]
        if not pdfs:
            return jsonify({'error': 'No PDF files found matching the criteria'}), 404

        output_filename = f"{emp}_merged.pdf"
        output_path = os.path.join(directory_path, output_filename)

        merger = PdfMerger()
        for pdf in pdfs:
            pdf_path = os.path.join(directory_path, pdf)
            try:
                reader = PdfReader(pdf_path)
                merger.append(reader)
            except Exception as merge_error:
                return jsonify({'error': f'Failed to merge {pdf}', 'details': str(merge_error)}), 500
            finally:
                # Close the PdfReader explicitly
                if 'reader' in locals():
                    reader.stream.close()

        try:
            merger.write(output_path)
        except Exception as write_error:
            return jsonify({'error': 'Failed to write the merged file', 'details': str(write_error)}), 500
        finally:
            merger.close()

        # Short delay to ensure the file handles are released
        time.sleep(1)
        gc.collect()

        # Attempt to delete the original PDF files
        for f in pdfs:
            file_path = os.path.join(directory_path, f)
            try:
                os.remove(file_path)
            except Exception as delete_error:
                return jsonify({'error': f'Failed to delete {f}', 'details': str(delete_error)}), 500

        return jsonify({'message': 'Conversion successful', 'merged_file': output_path}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
