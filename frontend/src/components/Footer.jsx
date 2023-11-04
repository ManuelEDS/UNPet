import React from 'react';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';

const styles = {
  footer: {
    backgroundColor: '#00C05D',
    color: 'white',
    padding: '20px 0',
    position: 'fixed',
    bottom: 0,
    width: '100%',
  },
};

export default function Footer() {
  return (
    <footer style={styles.footer}>
      <Container maxWidth="lg">
        <Box textAlign="center">
          <Typography variant="body2">
            Síguenos en las redes sociales:
          </Typography>
          <Box mt={2}>
            <Link href="https://twitter.com/UNPet2023" target="_blank" color="inherit" style={{ marginRight: '20px' }}>
              <TwitterIcon /> {/* Ícono de Twitter de Material-UI */}
            </Link>
            <Link href="https://www.instagram.com/unpet2023/" target="_blank" color="inherit">
              <InstagramIcon /> {/* Ícono de Instagram de Material-UI */}
            </Link>
          </Box>
        </Box>
      </Container>
    </footer>
  );
}
