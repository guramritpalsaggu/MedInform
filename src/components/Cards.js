import React from 'react';
import '../CSS/Card.css';
import skin from '../Images/skin.jpg';
import tuber from '../Images/Tuberculosis.jpg';
import Pneumonia from '../Images/Pneumonia.jpg';
import retina from '../Images/retinopathy.jpg';
import Malaria from '../Images/Malaria.jpg';

const Cards = () => {
	return(
    <section class="wrapper style1">
        <div class="inner z-2">
        <h1>Topic btao yha paas ka</h1>
          <article class="feature left">
            <span class="image"><img src={skin} alt="" /></span>
            <div class="content">
              <h1>Skin Cancer</h1>
              <p>Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero, faucibus adipiscing, commodo quis, gravida id, est.</p>
              <p className="read-more">
               <a href="https:medinform.tk">Go to Page</a>
              </p>
            </div>
          </article>
          <article class="feature right">
            <span class="image"><img src={tuber} alt="" /></span>
            <div class="content">
              <h1>Tuberculosis</h1>
              <p>Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero, faucibus adipiscing, commodo quis, gravida id, est.</p>
              <p className="read-more">
               <a href="#skin">Go to Page</a>
              </p>
            </div>
          </article>
          <article class="feature left">
            <span class="image"><img src={Pneumonia} alt="" /></span>
            <div class="content">
              <h1>Pneumonia</h1>
              <p>Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero, faucibus adipiscing, commodo quis, gravida id, est.</p>
              <p className="read-more">
               <a href="#skin">Go to Page</a>
              </p>
            </div>
          </article>
          <article class="feature right">
            <span class="image"><img src={retina} alt="" /></span>
            <div class="content">
              <h1>Retinopathy</h1>
              <p>Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero, faucibus adipiscing, commodo quis, gravida id, est.</p>
              <p className="read-more">
               <a href="#skin">Go to Page</a>
              </p>
            </div>
          </article>
          <article class="feature left">
            <span class="image"><img src={Malaria} alt="" /></span>
            <div class="content">
              <h1>Malaria</h1>
              <p>Sed egestas, ante et vulputate volutpat, eros pede semper est, vitae luctus metus libero eu augue. Morbi purus libero, faucibus adipiscing, commodo quis, gravida id, est.</p>
              <p className="read-more">
               <a href="#skin">Go to Page</a>
              </p>
            </div>
          </article>
        </div>
      </section>
	);
}

export default Cards;