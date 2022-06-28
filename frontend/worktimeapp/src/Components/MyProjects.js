// import React, { Component } from 'react';
// import InputLabel from '@mui/material/InputLabel';
// import MenuItem from '@mui/material/MenuItem';
// import Select from '@mui/material/Select';
// import Grid from '@mui/material/Grid'
// import Card from '@mui/material/Card';
// import Typography from '@mui/material/Typography';
// import AssignmentIcon from '@mui/icons-material/Assignment';
// import FormControl from '@mui/material/FormControl';
// import Paper from '@mui/material/Paper';
// import Table from '@mui/material/Table';
// import TableBody from '@mui/material/TableBody';
// import TableCell from '@mui/material/TableCell';
// import TableContainer from '@mui/material/TableContainer';
// import TableHead from '@mui/material/TableHead';
// import TablePagination from '@mui/material/TablePagination';
// import TableRow from '@mui/material/TableRow';



// class MyProjects extends Component {
    
//     constructor(props) {
//         super(props);

//         this.state = {
//           projectType: "",
//           time: Date
//       }
//   }
//   handleChange = (e) =>{
//       this.setState({ [e.target.name] : e.target.value });}

//   handleDateChange(newValue){
//       this.setState({
//           time: new Date(newValue)
//       })
//     }

//     render() { 
//         return (
          
//           <Card sx={{ m:5, p:2, minwidth: 500}}>
//             <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
//                   <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
//                     <Grid item >
//                       <AssignmentIcon></AssignmentIcon>
//                    </Grid>
//                   </Grid>
//                     <Grid item xs={12} sm={4} sx={{pb:1}}>
//                         <Typography variant="h5" component="div">
//                          My Projects
//                         </Typography>
//                         <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
//                         Your projects and tasks at the moment. 
//                         </Typography>
//                         </Grid>
//                 </Grid>
//                 <Grid container spacing={2}  alignItems="center">
//                   <Grid item xs={12} sm={12}>
//                        <FormControl sx={{ minWidth: 258}}>
//                           <InputLabel>Project 1</InputLabel>
//                           <Select
//                             name="projectType"
//                             value={this.state.projectType}
//                             label="Type"
//                             onChange={this.handleChange}
//                           >
//                             <MenuItem value={"task1"}>Task 1</MenuItem>
//                             <MenuItem value={"task2"}>Task 2</MenuItem>
//                           </Select>
//                         </FormControl>   
//                         <Grid container spacing={200}  alignItems="center">
//                     <Grid item xs={12} sm={12}>
//                        <FormControl sx={{ minWidth: 258}}>
//                           <InputLabel>Project 2</InputLabel>
//                           <Select
//                             name="projectType"
//                             value={this.state.projectType}
//                             label="Type"
//                             onChange={this.handleChange}
//                           >
//                             <MenuItem value={"task 1"}>Task 1</MenuItem>
//                             <MenuItem value={"task 2"}>Task 2</MenuItem>
//                           </Select>
//                         </FormControl>                   
//                      </Grid>
//                  </Grid>                
//               </Grid>
//             </Grid>
//           </Card>
          
        
//         );
//     }
// }
 
// export default MyProjects;
import React, { Component } from 'react';
import AssignmentIcon from '@mui/icons-material/Assignment';

import InboxIcon from '@mui/icons-material/MoveToInbox';
import DraftsIcon from '@mui/icons-material/Drafts';
import SendIcon from '@mui/icons-material/Send';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import StarBorder from '@mui/icons-material/StarBorder';
import {withStyles,
    Typography,
    Accordion,
    AccordionSummary,
    AccordionDetails,
    TextField,
    Button,
    List,
    ListItem,
    Box,
    Collapse,
    ListItemText,
    ListItemIcon,
    ListItemButton,
    ListSubheader,
    TableRow,
    TableHead,
    TableContainer,
    TableCell,
    TableBody,
    Table,
    Paper,
    FormControl,
    Card,
    Grid,
    Select,
    MenuItem,
    InputLabel
} from '@mui/material';

import { MyProjectpopup } from './MyProjectpopup';
import EditActivity from './Dialog/EditActivity';
import MyActivitiesEntry from './MyActivitiesEntry';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';

const header = [
  {
  id: 'name',
  name: 'Name',
  label: 'Name'
  },
  {
      id: 'commissioner',
      name: 'Commissioner',
      label: 'Commissioner'
  }, 
  {
      id: 'user',
      name: 'User',
      label: 'User'
  },
  {
      id: 'duration',
      name: 'Duration',
      label: 'Duration'
  },
]
const data = [
  {
      id: 1,
      name:'SW Project',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '90 Tage'
  },
  {
      id: 2,
      name:'Programmieren',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '999 Tage'
  },
  {
      id: 3,
      name:'Schlafen',
      commissioner: '',
      user: 'Susi',
      duration: '15 Tage'
  }
]

const activities = [
    {
        name: "Use Case erstellen",
        capacity: "45h"
    },
    {
        name: "ERM Diagram",
        capacity: "10h"
    },
    {
        name: "Blabla",
        capacity: "5h"
    },
]

/**
 * Projekte und Activities vom aktuellen User
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyProjects extends Component {
    
    constructor(props) {
        super(props);

        this.state = {
          userId : props.userId,
          projects : null,

          // projectType: "",
          // time: Date,

          showEditWindow: false,
          showEditActicity: false
      }

        //get Projects of current User
        //get Activities of these Projects
        /**
         * mögliche Form die Acticity Objekte zu holen:
         * {project id: [Liste der ActivityBOs]}
         */

  }

  editWindow = () => {
    this.setState({
      showEditWindow: true
    }, function(){
      console.log('Edit Window öffnen')
    })
  }

  closeDialog = (project) => {
    if(project){
      this.updateProject(project)
      this.setState({
        showEditWindow: false
      }, function(){
        console.log('Edit Window schließen')
      })
    }else{
      this.setState({
        showEditWindow:false
      }, function(){
        console.log('Edit Window schließen')
      })
    }
  }

  editWindowActivity = () => {
    this.setState({
      showEditActicity: true
    }, function(){
      console.log('Edit Window')
    })
  }

  closeDialogActivity = (activity) => {
    if(activity){
      this.updateProject(activity)
      this.setState({
        showEditActicity: false
      }, function(){
        console.log('Edit Window')
      })
    }else{
      this.setState({
        showEditWindow:false
      }, function(){
        console.log('Edit Window')
      })
    }
  }

  getProjects = () => {
    WorkTimeAppAPI.getAPI().getProjectsForUser(this.state.userId).then(projects =>
      this.setState({
        projects : projects
      })         
    )
  }

  updateProject = (project) => {
    
  }

  componentDidMount(){
    this.getProjects()
  }

  render(){
      return(
        <Card sx={{ m:5, p:2, minwidth: 500}}>
          {/* <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
            <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
              <Grid item >
                <AssignmentIcon></AssignmentIcon>
              </Grid>
            </Grid>
          <Grid item xs={12} sm={4} sx={{pb:1}}> */}
          <Typography variant="h5" component="div">
            <AssignmentIcon></AssignmentIcon>
            My Projects
          </Typography>
          <Typography sx={{ fontSize: 16 }} color="text.secondary" gutterBottom>
            Your projects and activities at the moment. 
          </Typography>

            {data.map((item) => (
                <Accordion>
                    <AccordionSummary>
                      {/* <Typography>
                        {item.id +"\t"+ item.name +"\t" }
                      </Typography> */}
                          <TableRow
                          >
                            <TableCell>
                              {"Project name: "+item.name}
                            </TableCell>
                            {/* <TableCell align="right">{item.user}
                            </TableCell> */}
                            <TableCell align="right">{"Commisioner: "+item.commissioner}</TableCell>
                            {/* <TableCell align="right">{item.duration}</TableCell> */}
                          </TableRow>
                    </AccordionSummary>
                    <AccordionDetails>
                      <List>
                        <Table>
                        <TableHead>
                          <TableRow>
                            <TableCell>Activities</TableCell>
                            <TableCell align="left">Capacity</TableCell>
                            <TableCell></TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          <MyActivitiesEntry projectId = {item.id}></MyActivitiesEntry>
                          {/* {activities.map((activity) => (
                            <MyActivitiesEntry projectId = {item.id}></MyActivitiesEntry>
                          ))} */}
                        </TableBody>
                        {/* {activities.map((elem) => (
                          <TableRow
                            hover
                            onClick = {this.editWindowActicity}
                          >
                            <TableCell>
                                {elem.name}
                            </TableCell>
                            <TableCell>
                                {elem.capacity}
                            </TableCell>
                            <EditActivity show={this.state.showEditActicity} onClose={this.closeDialogActivity}></EditActivity>
                          </TableRow>
                          
                        
                        ))} */}
                        </Table>
                    </List>
                    <MyProjectpopup show={this.state.showEditWindow} onClose={this.closeDialog} project={item}></MyProjectpopup>
                </AccordionDetails>
            </Accordion>
        ))}

    {/* </Grid>
    </Grid> */}
  </Card>
      )
  }
}
export default MyProjects