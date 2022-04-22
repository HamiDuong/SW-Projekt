import * as React from 'react';
import { styled, alpha } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import InputBase from '@mui/material/InputBase';
import MenuIcon from '@mui/icons-material/Menu';
import SearchIcon from '@mui/icons-material/Search';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
 
// Suchleiste
 
// const Search = styled('div')(({ theme }) => ({
//   position: 'relative',
//   borderRadius: theme.shape.borderRadius,
//   backgroundColor: alpha(theme.palette.common.white, 0.15),
//   '&:hover': {
//     backgroundColor: alpha(theme.palette.common.black, 0.25),
//   },
//   marginLeft: 0,
//   width: '100%',
//   [theme.breakpoints.up('sm')]: {
//     marginLeft: theme.spacing(1),
//     width: 'auto',
//   },
// }));
 
// const SearchIconWrapper = styled('div')(({ theme }) => ({
//   padding: theme.spacing(0, 2),
//   height: '100%',
//   position: 'absolute',
//   pointerEvents: 'none',
//   display: 'flex',
//   alignItems: 'center',
//   justifyContent: 'center',
// }));
 
// const StyledInputBase = styled(InputBase)(({ theme }) => ({
//   color: 'black',
//   '& .MuiInputBase-input': {
//     padding: theme.spacing(1, 1, 1, 0),
//     // vertical padding + font size from searchIcon
//     paddingLeft: `calc(1em + ${theme.spacing(4)})`,
//     transition: theme.transitions.create('width'),
//     width: '100%',
//     [theme.breakpoints.up('sm')]: {
//       width: '12ch',
//       '&:focus': {
//         width: '20ch',
//       },
//     },
//   },
// }));
 
 
 
export default function Navigator() {
 const [anchorEl , setAnchorEl] = React.useState(null)
  const handleClose = () => {
   setAnchorEl(null)
 }
  const openMenu = (event) => {
   setAnchorEl(event.currentTarget)
 }
 return (
   <Box sx={{ flexGrow: 1 }}>
     <AppBar position="static">
       <Toolbar>
         <IconButton
           size="large"
           edge="start"
           color="inherit"
           aria-label="open drawer"
           sx={{ mr: 2 }}
         >
         <Button
           variant = "container"
           onClick = {openMenu}
           >
         <MenuIcon />
         </Button>
         <Menu
         id = "menu"
         anchorEl={anchorEl}
         keepMounted
         open={Boolean(anchorEl)}
         onClose={handleClose}
         >
           <MenuItem onClick={handleClose}>Profil</MenuItem>
           <MenuItem onClick={handleClose}>Zeitkonto</MenuItem>
         </Menu>
         </IconButton>
         <Typography
           variant="h6"
           noWrap
           component="div"
           sx={{ flexGrow: 1, display: { xs: 'none', sm: 'block' } }}
         >
           WorkTimeApp (Platzhalter)
         </Typography>
         {/* <Search>
           <SearchIconWrapper>
             <SearchIcon />
           </SearchIconWrapper>
           <StyledInputBase
             placeholder="Suche…"
             inputProps={{ 'aria-label': 'search' }}
           />
         </Search> */}
       </Toolbar>
     </AppBar>
   </Box>
 );
}
