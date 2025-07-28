# 🚗 Car Move

A comprehensive web-based management system for car showrooms built with Django. This system allows showroom managers to efficiently manage their car inventory while providing customers with an intuitive interface to browse and explore available vehicles.

## 🌟 Features

### 🔧 Core Features
- **Car Management**: Add, edit, and delete car listings
- **Image Upload**: Support for front and back car images
- **Detailed Car Information**: Name, model, year, price, brand, and description
- **Brand Management**: Organize cars by different brands
- **Search & Filter**: Advanced search capabilities
- **Responsive Design**: Mobile-friendly interface

### 🚀 Advanced Features
- **3D Model Support**: Integration for 3D car models
- **Admin Dashboard**: Comprehensive admin interface
- **Image Gallery**: Multiple images per car
- **Car Comparison**: Compare different vehicles
- **User Authentication**: Secure login system

## 🛠️ Tech Stack

- **Backend**: Django 4.x, Python 3.8+
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (Dev) 
- **File Storage**: Django Media Files

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/car-move.git
cd car-move
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application!

## 📁 Project Structure

```
car-move/
├── 📁 car_move/              # Main project directory
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── 📁 cars/                 # Cars app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── urls.py              # App URLs
│   └── 📁 templates/        # HTML templates
├── 📁 media/                # Uploaded files
│   └── 📁 car_images/       # Car images
├── 📁 static/               # Static files
│   ├── 📁 css/              # Stylesheets
│   ├── 📁 js/               # JavaScript files
│   └── 📁 images/           # Static images
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🗄️ Database Models

### Car Model
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Car name |
| model | CharField | Car model |
| year | IntegerField | Manufacturing year |
| price | DecimalField | Car price |
| brand | ForeignKey | Car brand |
| description | TextField | Car description |
| front_image | ImageField | Front car image |
| back_image | ImageField | Back car image |
| model_3d_url | URLField | 3D model URL |
| created_at | DateTimeField | Creation timestamp |
| updated_at | DateTimeField | Last update timestamp |

### Brand Model
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Brand name |
| logo | ImageField | Brand logo |
| created_at | DateTimeField | Creation timestamp |

## 🔧 Usage

### Adding a New Car
1. Navigate to `/cars/add/`
2. Fill in all required fields
3. Upload front and back images
4. Optionally add a 3D model URL
5. Click "Save Car"

### Managing Brands
1. Access the admin panel at `/admin/`
2. Navigate to "Brands" section
3. Add, edit, or delete brands as needed

### Browsing Cars
1. Visit the homepage
2. Browse all available cars
3. Click on any car for detailed view
4. Use search and filter options

## 🎨 Screenshots

*Add screenshots of your application here*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the amazing framework
- Bootstrap team for the responsive CSS framework
- Contributors and testers

## 📞 Contact

Your Name - your.email@example.com

Project Link: ([https://github.com/yourusername/car-move](https://github.com/Moh0py/UNIT-PROJECT-2.git))

---

⭐ **Star this repository if you found it helpful!**
