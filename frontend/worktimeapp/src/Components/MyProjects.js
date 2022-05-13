import React, { Component } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';
import AssignmentIcon from '@mui/icons-material/Assignment';
import FormControl from '@mui/material/FormControl';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';

class MyProjects extends Component {
    constructor(props) {
        super(props);

        this.state = {
          projectType: "",
          time: Date
      }
  }
  handleChange = (e) =>{
      this.setState({ [e.target.name] : e.target.value });}

  handleDateChange(newValue){
      this.setState({
          time: new Date(newValue)
      })
    }

    render() { 
        return (
          
          <Card sx={{ m:5, p:2, minwidth: 500}}>
            <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                  <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                    <Grid item >
                      <AssignmentIcon></AssignmentIcon>
                   </Grid>
                  </Grid>
                    <Grid item xs={12} sm={4} sx={{pb:1}}>
                        <Typography variant="h5" component="div">
                         My Projects
                        </Typography>
                        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                        Your projects and tasks at the moment. 
                        </Typography>
                        </Grid>
                </Grid>
                <Grid container spacing={2}  alignItems="center">
                  <Grid item xs={12} sm={12}>
                       <FormControl sx={{ minWidth: 258}}>
                          <InputLabel>Project 1</InputLabel>
                          <Select
                            name="projectType"
                            value={this.state.projectType}
                            label="Type"
                            onChange={this.handleChange}
                          >
                            <MenuItem value={"task1"}>Task 1</MenuItem>
                            <MenuItem value={"task2"}>Task 2</MenuItem>
                          </Select>
                        </FormControl>   
                        <Grid container spacing={200}  alignItems="center">
                    <Grid item xs={12} sm={12}>
                       <FormControl sx={{ minWidth: 258}}>
                          <InputLabel>Project 2</InputLabel>
                          <Select
                            name="projectType"
                            value={this.state.projectType}
                            label="Type"
                            onChange={this.handleChange}
                          >
                            <MenuItem value={"task 1"}>Task 1</MenuItem>
                            <MenuItem value={"task 2"}>Task 2</MenuItem>
                          </Select>
                        </FormControl>                   
                     </Grid>
                 </Grid>                
              </Grid>
            </Grid>
          </Card>
          
        
        );
    }
}
 
export default MyProjects;
