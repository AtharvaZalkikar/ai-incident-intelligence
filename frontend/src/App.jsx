import MainLayout from "./layouts/MainLayout";
import Header from "./components/Header";
import Dashboard from "./pages/Dashboard";


function App() {
  return (
    <MainLayout>
      <Header />
      <Dashboard />
    </MainLayout>
  );
}

export default App;