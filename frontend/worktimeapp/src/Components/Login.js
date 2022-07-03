import React, { Component } from 'react';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';

class Login extends Component {
    constructor(props) {
        super(props);
    }
    
	handleSignInButtonClicked = () => {
		this.props.onLogIn();
	}
    render() { 
        return (
            <div>
				<Card sx={{ m:5, p:2}}>

				<Grid container direction="column"  justify="space-between" alignItems="center" spacing={2}>
					<Typography variant="h4">Welcome!</Typography>
					<Grid item>
						<Button variant='contained' color='primary' onClick={this.handleSignInButtonClicked}>
							Login
      			</Button>
                	</Grid> 
				</Grid>
			</Card>

			</div>
          );
    }
}
 
export default Login ;