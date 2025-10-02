#!/usr/bin/env python3
"""
HTML to DOCX Converter - Test Script
Run this script to test the HTML to DOCX conversion functionality
"""

from html_to_docx_converter import convert_html_string_to_docx, convert_html_file_to_docx
import os

def test_basic_conversion():
    """Test basic HTML to DOCX conversion"""
    
    print("🔄 Testing HTML to DOCX Converter")
    print("=" * 50)
    
    # Sample HTML content
    html_content = """
    <html>
    <head>
        <title>Test Document</title>
    </head>
    <body>
        <h1>Welcome to HTML to DOCX Converter</h1>
        <p>This is a <strong>test document</strong> that demonstrates the conversion of <em>HTML</em> content to <u>Microsoft Word</u> format.</p>
        
        <h2>Features Supported:</h2>
        <ul>
            <li><strong>Bold text</strong></li>
            <li><em>Italic text</em></li>
            <li><u>Underlined text</u></li>
            <li>Links: <a href="https://python.org">Python.org</a></li>
            <li>Code formatting: <code>print("Hello World")</code></li>
        </ul>
        
        <h3>Sample Table</h3>
        <table>
            <tr>
                <th>Feature</th>
                <th>Supported</th>
            </tr>
            <tr>
                <td>Headings</td>
                <td>✅ Yes</td>
            </tr>
            <tr>
                <td>Tables</td>
                <td>✅ Yes</td>
            </tr>
            <tr>
                <td>Lists</td>
                <td>✅ Yes</td>
            </tr>
        </table>
        
        <p>This converter handles most common HTML elements and converts them to properly formatted Word documents.</p>
    </body>
    </html>
    """
    
    try:
        # Convert HTML string to DOCX
        output_file = convert_html_string_to_docx(html_content, "test_output.docx")
        
        print(f"✅ Conversion successful!")
        print(f"📄 Output file created: {output_file}")
        print(f"📍 Full path: {os.path.abspath(output_file)}")
        print(f"📊 File size: {os.path.getsize(output_file):,} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ Conversion failed: {str(e)}")
        return False

def demo_usage_examples():
    """Demonstrate different usage examples"""
    
    print(f"\n💡 USAGE EXAMPLES")
    print("=" * 50)
    
    print("""
    # Example 1: Convert HTML string to DOCX
    from html_to_docx_converter import convert_html_string_to_docx
    
    html_content = "<h1>Hello World</h1><p>This is a test.</p>"
    output_file = convert_html_string_to_docx(html_content, "output.docx")
    
    # Example 2: Convert HTML file to DOCX
    from html_to_docx_converter import convert_html_file_to_docx
    
    output_file = convert_html_file_to_docx("input.html", "output.docx")
    
    # Example 3: Use the converter class directly
    from html_to_docx_converter import HTMLToDOCXConverter
    
    converter = HTMLToDOCXConverter()
    output_file = converter.convert_html_to_docx(html_content, "output.docx")
    """)

if __name__ == "__main__":
    # Run the test
    success = test_basic_conversion()
    
    if success:
        demo_usage_examples()
        print(f"\n🎉 Test completed successfully!")
        print(f"   You can now open 'test_output.docx' to see the converted document.")
    else:
        print(f"\n❌ Test failed. Please check the error messages above.")