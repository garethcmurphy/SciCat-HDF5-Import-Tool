# SciCat HDF5 Import Tool 🐍📊  

This repository provides a tool for importing **HDF5 raw data** into the **SciCat data catalog** used at the **European Spallation Source (ESS)**. It also supports metadata harvesting to ensure comprehensive data cataloging.

---

## Features ✨  

- **HDF5 Import**: Automatically imports raw data files into SciCat.  
- **Metadata Harvesting**: Extracts and registers metadata for datasets.  
- **Integration Ready**: Seamlessly connects with the SciCat API.  

---

## Prerequisites 🛠️  

- Python 3.8+  
- Required libraries:
  - `h5py`  
  - `requests`  

Install dependencies:  
pip install h5py requests  

---

## Installation  

1. Clone the repository:  
   git clone https://github.com/your-username/scicat-hdf5-import.git  
   cd scicat-hdf5-import  

2. Install dependencies:  
   pip install -r requirements.txt  

---

## Usage 🔧  

1. Update the `config.json` file with:  
   - SciCat API endpoint.  
   - Authentication token.  

2. Import HDF5 data:  
   python import_hdf5.py --file <path-to-hdf5-file>  

3. Monitor logs for import status and errors.  

---

## File Structure 📂  

- `import_hdf5.py`: Main script for importing HDF5 data.  
- `config.json`: Configuration for SciCat API and metadata settings.  
- `requirements.txt`: Python dependencies.  
- `README.md`: Documentation for the repository.  

---

## Example Commands  

- Import an HDF5 file:  
  python import_hdf5.py --file example.h5  

- View metadata extraction:  
  python import_hdf5.py --file example.h5 --verbose  

---

## Contributing 🤝  

1. Fork the repository.  
2. Create a new branch:  
   git checkout -b feature/your-feature  

3. Commit your changes:  
   git commit -m "Add your feature"  

4. Push the branch:  
   git push origin feature/your-feature  

5. Open a pull request.  

---

## License 📝  

This project is licensed under the MIT License. See the LICENSE file for details.  

---

**Effortlessly import HDF5 data and harvest metadata with this SciCat tool!** 🐍📊  
