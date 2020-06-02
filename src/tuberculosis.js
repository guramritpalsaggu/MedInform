import React, {useEffect, useState} from 'react';
import {useDropzone} from 'react-dropzone';
import './input.css'
const thumbsContainer = {
  display: 'flex',
  flexDirection: 'row',
  flexWrap: 'wrap',
  marginTop: 16,
  background : 'aliceblue',
  maxWidth: '600px'
};

const thumb = {
  display: 'inline-flex',
  borderRadius: 2,
  border: '1px solid #eaeaea',
  marginBottom: 8,
  marginRight: 8,
  width: 100,
  height: 100,
  padding: 4,
  boxSizing: 'border-box'
};

const thumbInner = {
  display: 'flex',
  minWidth: 0,
};

const img = {
  display: 'block',
  width: 'auto',
  height: '100%',
  margin:'1% 6%',
};


function Previews(props) {
  const [files, setFiles] = useState([]);
  const {acceptedFiles,getRootProps, getInputProps} = useDropzone({
    accept: 'image/*',
    onDrop: acceptedFiles => {
      setFiles(acceptedFiles.map(file => Object.assign(file, {
        preview: URL.createObjectURL(file)
      })));
    }
  });
  
  const thumbs = files.map(file => (
    <div style={thumb} key={file.name}>
      <div style={thumbInner}>
        <img
          src={file.preview}
          style={img}
        />
        <p> {file.name} </p>
      </div>
    </div>
  ));
  useEffect(() => () => {
    // Make sure to revoke the data uris to avoid memory leaks
    files.forEach(file => URL.revokeObjectURL(file.preview));
  }, [files]);

  return (
    <div className="main">
    <h1 className="head"> Topic for this page </h1>
    <section className="container">
      <div {...getRootProps({className: 'dropzone'})}>
        <input {...getInputProps()} />
        <p className="cont">Drag and drop image here, or<strong className="f4 mr1 ml1"> click  </strong> to select image</p>
      </div>
    </section>
    <aside style={thumbsContainer}>
        {thumbs}
    </aside>
    <button class="fl mt2 pointer dim ph3 pv2 mb2 dib bg-dark-blue shadow-3-1 br3" href="#0">SUBMIT</button>
    </div>
  );
}

export default Previews;