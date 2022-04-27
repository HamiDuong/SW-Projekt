import { createTheme } from '@mui/material/styles';
import { indigo, blue, green, orange, red, blueGrey, grey, deepPurple} from '@mui/material/colors';

const white = '#FFFFFF';
const black = '#000000';

// A custom theme for this app
const theme = createTheme({
  palette: {
    black,
    white,
    primary: {
      contrastText: white,
      dark: deepPurple[900],
      main: deepPurple[500],
      light: indigo[100]
    },
    secondary: {
      contrastText: white,
      dark: blue[900],
      main: blue[200],
      light: blue['A400']
    },
    success: {
      contrastText: white,
      dark: green[900],
      main: green[600],
      light: green[400]
    },
    info: {
      contrastText: white,
      dark: blue[900],
      main: blue[600],
      light: blue[400]
    },
    warning: {
      contrastText: white,
      dark: orange[900],
      main: orange[600],
      light: orange[400]
    },
    error: {
      contrastText: white,
      dark: red[900],
      main: red[600],
      light: red[400]
    },
    text: {
      primary: blueGrey[800],
      secondary: blueGrey[600],
      link: blue[600]
    },
    background: {
      default: blue[50],
      paper: white
    },
    icon: "#9c27b0",
    divider: grey[200]
  }, 
});



export default theme;