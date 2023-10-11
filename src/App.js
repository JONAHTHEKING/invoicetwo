import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import InvoiceList from './components/InvoiceList/InvoiceList';
import InvoiceForm from "./components/InvoiceForm/InvoiceForm";
import InvoiceItems from "./components/InvoiceItems/InvoiceItems";
import ItemForm from "./components/ItemForm/ItemForm";
import PrivateRoute from './components/PrivateRoute/PrivateRoute';
import Login from './components/Login/Login';
import Signup from './components/Signup/Signup';
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='' element={<PrivateRoute child={<InvoiceList />} />}>
          </Route>
          <Route path='newInvoice' element={<PrivateRoute child={<InvoiceForm />} />}>
          </Route>
          <Route path='/:id' element={<PrivateRoute child={<InvoiceItems />} />}>
          </Route>
          <Route path='/:id/newItem' element={<PrivateRoute child={<ItemForm />} />}>
          </Route>
          <Route path="login/" element={<Login />} />
          <Route path="signup/" element={<Signup />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
