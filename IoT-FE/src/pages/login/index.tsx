import { AuthPage, ThemedTitleV2 } from "@refinedev/mui";
import { AppIcon } from "../../components/app-icon";

export const Login = () => {
  return (
    <AuthPage
      type="login"
      title={
        <ThemedTitleV2
          collapsed={false}
          text="IoT Project"
          icon={<AppIcon />}
        />
      }
    />
  );
};
