import React from 'react';
import brain from './med.png';
const logo =() =>{
	return (	 
		<div className='ma4'>
			<div className="Tilt br2 shadow-2" options={{ max : 25 }} style={{ height: 100, width: 100 }} >
				 <div className="Tilt-inner pa3"> <img src={brain} alt=' ' /></div>
			</div>
		</div>
	);
}

export default logo;