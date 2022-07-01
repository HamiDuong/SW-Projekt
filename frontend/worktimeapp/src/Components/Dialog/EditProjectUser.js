class EditProjectUser extends Component {
    constructor(props){
        super(props);
        this.state = {

        }
        this.baseState = this.state;
    }
    
    render() {
        const {show} = this.props 
        return (
            show ?
            <Dialog>

            </Dialog>
            :null
        );
    }
}
 
export default EditProjectUser;