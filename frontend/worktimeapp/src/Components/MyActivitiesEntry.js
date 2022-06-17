import React, { Component } from 'react';
import { TableCell, TableRow } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import MyProjectsEntry from './MyProjectsEntry';


class MyActivitiesEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activity : props.activity,
            showDialog: false,
            openPopup:false,
            setOpenPopup:false
        }
    }
    showEdit = () => {
        this.setState({
            showDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }

    closeDialog = (booking) => {
        if(booking){
            this.updateBooking(booking)
            this.setState({
                showDialog: false
            }, function(){
                console.log("Editwindow wird geschlossen")
            })
        }else{
            this.setState({
                showDialog: false
            },function(){
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }
    // togglePopupActivities() {
    //     this.setState({
    //       showPopupAddActivities: !this.state.showPopupAddActivities,
    //     });
    //   }


    render() { 
        const  {openPopup, setOpenPopup } =  this.state
        return (
            <>
                <TableRow
                    hover
                    onClick = {this.showEdit}
                >
                    <TableCell>{this.state.activity.name}</TableCell>
                    <TableCell>{this.state.activity.capacity}</TableCell>
                    <TableCell><button className='openPopup' onClick={() => {
                            setOpenPopup(true);
                             } }>
                             Öffnen
                           </button>
                       
                         

                        
                    </TableCell>
                    {/* <TableCell> {this.state.setOpenPopup(true)= ()=>{
                       <button className='openPopup' onClick={() => {
                            setOpenPopup(true);
                       } }>
                     Öffnen
                           </button> 
                    }}  
                     {openPopup && <MyProjectsEntry closePopup={setOpenPopup}/>}</TableCell> */}
                </TableRow>
                {/* <MyProjectsEntry show={this.state.showDialog} onClose={this.closeDialog}></MyProjectsEntry> */}
            
            </>
        );
    }
}
 
export default MyActivitiesEntry;