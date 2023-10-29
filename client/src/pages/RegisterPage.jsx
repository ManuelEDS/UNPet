import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { Link } from 'react-router-dom'
import Grid from '@mui/material/Grid';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { FormControl } from '@mui/material';
import  { useState } from 'react';
import {register} from '../api/accounts.api'

const defaultTheme = createTheme();
const tiposDocumento = [
  { value: 'CC', label: 'Cédula de Ciudadanía (CC)' },
  { value: 'TI', label: 'Tarjeta de Identidad (TI)' },
  { value: 'CE', label: 'Cédula de Extranjería (CE)' },
  { value: 'Pasaporte', label: 'Pasaporte' },
  // Agrega más tipos de documento según sea necesario
];
const sexoOptions = [
  { value: 'M', label: 'Masculino' },
  { value: 'F', label: 'Femenino' },
  { value: 'O', label: 'Otro' },
];
export const localidades = [
  { id: '1', name: 'Usaquén' },
  { id: '2', name: 'Chapinero' },
  { id: '3', name: 'Santa Fe' },
  { id: '4', name: 'San Cristóbal' },
  { id: '5', name: 'Usme' },
  { id: '6', name: 'Tunjuelito' },
  { id: '7', name: 'Bosa' },
  { id: '8', name: 'Kennedy' },
  { id: '9', name: 'Fontibón' },
  { id: '10', name: 'Engativá' },
  { id: '11', name: 'Suba' },
  { id: '12', name: 'Barrios Unidos' },
  { id: '13', name: 'Teusaquillo' },
  { id: '14', name: 'Los Mártires' },
  { id: '15', name: 'Antonio Nariño' },
  { id: '16', name: 'Puente Aranda' },
  { id: '17', name: 'La Candelaria' },
  { id: '18', name: 'Rafael Uribe Uribe' },
  { id: '19', name: 'Ciudad Bolívar' },
  { id: '20', name: 'Sumapaz' },
  // Agrega más localidades según sea necesario
];

export function Register() {

  const [tipoDocumento, setTipoDocumento] = useState('');
  const [sexo, setSexo] = useState('');
  const [localidad, setLocalidad] = useState('');
  const [errorUsername, setErrorUsername] = useState('');
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const usernameRegex = /^[a-zA-Z0-9_]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;

    if (!usernameRegex.test(data.username)) {
      setErrorUsername({message:'El nombre de usuario solo puede contener letras, números y guiones bajos.'});
    } else {
      setErrorUsername('');
    }

    if (!emailRegex.test(data.get('email'))) {
      setErrorEmail({message:'Ingrese una dirección de correo electrónico válida.'});
    } else {
      setErrorEmail('');
    }

    if (!passwordRegex.test(data.get('password'))) {
      setErrorPassword({message:'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.'});
    } else {
      setErrorPassword('');
    }

    if (usernameRegex.test(data.username) && emailRegex.test(data.get('email')) && passwordRegex.test(data.get('password'))) {
      console.log({
        email: data.get('email'),
        password: data.get('password'),
      });
      console.log(register(data));
    }
  };


  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <img src="/user-img-default.png" alt="User" width="40" height="40" />
          </Avatar>
          <Typography component="h1" variant="h5">
            Registrarse
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="given-name"
                  name="first_name"
                  required
                  fullWidth
                  id="first_name"
                  label="Primer Nombre"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="last_name"
                  label="Segundo Nombre"
                  name="last_name"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel id="tipo_doc-label">Tipo de Documento</InputLabel>
                  <Select
                    labelId="tipo_doc-label"
                    id="tipo_doc"
                    name="tipo_doc"
                    label="Tipo de Documento"
                    value={tipoDocumento}
                    onChange={(e) => setTipoDocumento(e.target.value)}
                  >
                    {tiposDocumento.map((tipo, index) => (
                      <MenuItem key={'k-tipo-d'+ index} value={tipo.value}>
                        {tipo.label}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>
              <Grid>
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="n_doc"
                  label="Número de documento"
                  name="n_doc"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel id="sexo-label">Sexo</InputLabel>
                  <Select
                    labelId="sexo-label"
                    id="sexo"
                    name="sexo"
                    label="Sexo"
                    value={sexo}
                    onChange={(e) => setSexo(e.target.value)}
                  >
                    {sexoOptions.map((option, index) => (
                      <MenuItem key={'k-sexo'+ index} value={option.value}>
                        {option.label}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="telefono"
                  label="Teléfono"
                  name="telefono"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel id="localidad-label">Localidad</InputLabel>
                  <Select
                    labelId="localidad-label"
                    id="idlocalidad"
                    name="idlocalidad"
                    label="Localidad"
                    value={localidad}
                    onChange={(e) => setLocalidad(e.target.value)}
                  >
                    {localidades.map((loc) => (
                      <MenuItem key={'k-loc'+ loc.id} value={loc.id}>
                        {loc.name}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12} sm={6}>
                <input
                  type="file"
                  name="photo_file"
                  accept="image/*" // Define el tipo de archivo aceptado (imágenes)
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Correo electrónico"
                  name="email"
                  autoComplete="email"
                  error={''!=errorEmail}
                  helperText={errorEmail ? errorEmail.message : ''}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="given-name"
                  name="username"
                  required
                  fullWidth
                  id="username"
                  label="Nombre de usuario"
                  
                  error={''!=errorUsername}
                  helperText={errorUsername ? errorUsername.message : ''}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Contraseña"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                  error={''!=errorPassword}
                  helperText={errorPassword ? errorPassword.message : ''}
                />
              </Grid>
              <Grid item xs={12}>
                <FormControlLabel
                  control={<Checkbox value="allowExtraEmails" color="primary" />}
                  label="Estoy de acuerdo con los términos y condiciones del servicio"
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Registrarse
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link to="/login">
                  Ya tienes una cuenta? Ingresa
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
