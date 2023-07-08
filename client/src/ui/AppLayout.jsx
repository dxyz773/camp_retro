import Header from "./Header";
// import Loading from "./Loading";
import { Outlet } from "react-router-dom";
// const navigation = useNavigation();
// const isLoading = navigation.state === "loading";
// {isLoading && <Loading />}
function AppLayout() {
  return (
    <div>
      <Header />
      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default AppLayout;
