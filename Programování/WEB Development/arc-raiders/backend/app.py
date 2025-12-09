"""
ARC Raiders - Flask Backend API
Simple Python backend for serving game data and handling contact form
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)  # Enable CORS for frontend requests

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# ============================================
# UTILITY FUNCTIONS
# ============================================

def load_json_file(filename):
    """Load JSON data from file"""
    try:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def save_contact_message(data):
    """Save contact form submission to file"""
    try:
        # Create contacts directory if it doesn't exist
        contacts_dir = os.path.join(BASE_DIR, 'contacts')
        os.makedirs(contacts_dir, exist_ok=True)
        
        # Add timestamp
        data['timestamp'] = datetime.now().isoformat()
        
        # Save to file
        filename = f"contact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(contacts_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"Error saving contact message: {e}")
        return False

# ============================================
# API ROUTES
# ============================================

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('..', 'index.html')

@app.route('/api/classes', methods=['GET'])
def get_classes():
    """Get all character classes"""
    classes = load_json_file('classes.json')
    
    if classes is None:
        return jsonify({'error': 'Failed to load classes data'}), 500
    
    return jsonify(classes)

@app.route('/api/classes/<int:class_id>', methods=['GET'])
def get_class(class_id):
    """Get specific class by ID"""
    classes = load_json_file('classes.json')
    
    if classes is None:
        return jsonify({'error': 'Failed to load classes data'}), 500
    
    # Find class by ID
    class_data = next((c for c in classes if c['id'] == class_id), None)
    
    if class_data is None:
        return jsonify({'error': 'Class not found'}), 404
    
    return jsonify(class_data)

@app.route('/api/weapons', methods=['GET'])
def get_weapons():
    """Get all weapons and equipment"""
    weapons = load_json_file('weapons.json')
    
    if weapons is None:
        return jsonify({'error': 'Failed to load weapons data'}), 500
    
    return jsonify(weapons)

@app.route('/api/weapons/<int:weapon_id>', methods=['GET'])
def get_weapon(weapon_id):
    """Get specific weapon by ID"""
    weapons = load_json_file('weapons.json')
    
    if weapons is None:
        return jsonify({'error': 'Failed to load weapons data'}), 500
    
    # Find weapon by ID
    weapon_data = next((w for w in weapons if w['id'] == weapon_id), None)
    
    if weapon_data is None:
        return jsonify({'error': 'Weapon not found'}), 404
    
    return jsonify(weapon_data)

@app.route('/api/news', methods=['GET'])
def get_news():
    """Get all news articles"""
    news = load_json_file('news.json')
    
    if news is None:
        return jsonify({'error': 'Failed to load news data'}), 500
    
    # Optional: Filter by category
    category = request.args.get('category')
    if category:
        news = [n for n in news if n['category'].lower() == category.lower()]
    
    # Optional: Limit number of results
    limit = request.args.get('limit', type=int)
    if limit:
        news = news[:limit]
    
    return jsonify(news)

@app.route('/api/news/<int:news_id>', methods=['GET'])
def get_news_item(news_id):
    """Get specific news article by ID"""
    news = load_json_file('news.json')
    
    if news is None:
        return jsonify({'error': 'Failed to load news data'}), 500
    
    # Find news by ID
    news_item = next((n for n in news if n['id'] == news_id), None)
    
    if news_item is None:
        return jsonify({'error': 'News article not found'}), 404
    
    return jsonify(news_item)

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Save the message
        if save_contact_message(data):
            return jsonify({
                'success': True,
                'message': 'Zpráva byla úspěšně odeslána!'
            }), 200
        else:
            return jsonify({'error': 'Failed to save message'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get general game statistics"""
    stats = {
        'total_classes': len(load_json_file('classes.json') or []),
        'total_weapons': len(load_json_file('weapons.json') or []),
        'total_news': len(load_json_file('news.json') or []),
        'server_status': 'online',
        'version': '2.0.0'
    }
    
    return jsonify(stats)

# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 ARC Raiders Backend Server")
    print("=" * 50)
    print(f"📁 Base Directory: {BASE_DIR}")
    print(f"📊 Data Directory: {DATA_DIR}")
    print("🌐 Server starting on http://localhost:5000")
    print("=" * 50)
    print("\nAvailable endpoints:")
    print("  GET  /api/classes")
    print("  GET  /api/classes/<id>")
    print("  GET  /api/weapons")
    print("  GET  /api/weapons/<id>")
    print("  GET  /api/news")
    print("  GET  /api/news/<id>")
    print("  POST /api/contact")
    print("  GET  /api/stats")
    print("\n" + "=" * 50)
    
    # Run the server
    app.run(debug=True, host='0.0.0.0', port=5000)
