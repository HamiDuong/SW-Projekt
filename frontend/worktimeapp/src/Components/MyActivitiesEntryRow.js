class MyActivitiesEntryRow extends Component {
    state = {  } 
    render() { 
        return (
            <TableRow
            hover
            onClick = {this.showEdit}
            >
                <TableCell>{elem.name}</TableCell>
                <TableCell>{elem.capacity}</TableCell>
                <TableCell>
                    <Button variant="contained" onClick={this.togglePopupMyProjectsEntry.bind(this)}>start</Button>
                    {this.state.showPopupMyProjectEntry ? 
                    <MyProjectsEntry
                    text='Close'
                    closePopup={this.togglePopupMyProjectsEntry.bind(this)}
                    // user={this.state.currentUser} workTimeAccount = {this.state.workTimeAccountId} 
                    activity = {elem}
                    userId={this.state.userId}
                    />
                    : null
                    }
                </TableCell>
            </TableRow>
        );
    }
}
 
export default MyActivitiesEntryRow;