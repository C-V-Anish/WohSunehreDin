import LinkedInIcon from '@mui/icons-material/LinkedIn';
import GitHubIcon from '@mui/icons-material/GitHub';
import InstagramIcon from '@mui/icons-material/Instagram';
import React from 'react';
import '../css/Footer.css';
import { Typography } from '@mui/material';

export const Footer = () => {
  return (
    <footer className="footer">
      <div className="icon-container">
        <LinkedInIcon sx={{fontSize:32,mt:7.5,marginRight:'20px'}} />
        <GitHubIcon sx={{fontSize:32,mt:7.5,marginRight:'20px'}} />
        <InstagramIcon sx={{fontSize:32,mt:7.5,marginRight:'20px'}} />
      </div>
    </footer>
  );
};
