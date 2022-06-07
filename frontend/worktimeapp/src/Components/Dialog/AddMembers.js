import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 


class AddMembers extends Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return ( 
            <Box
            component="form"
             sx={{
             '& > :not(style)': { m: 1, width: '25ch' },
                }}
            noValidate
            autoComplete="off">
            <div className='popup'>
                <div className='popup_inner'>
                
                <TextField id="outlined-basic" label="first name" variant="outlined" />
                <br/>
                <TextField id="outlined-basic" label="last name" variant="outlined" />
                <Grid xs={12} item>
                    <Button variant="contained" onClick={this.addProject}>Add Member</Button>
                </Grid>
                <Grid xs={12} item>
                    <Button variant="contained" onClick={this.props.closePopupMembers}>Close</Button>
                </Grid>
                </div>
               
            </div>
             </Box>
         );
    }
}
 
export default AddMembers;