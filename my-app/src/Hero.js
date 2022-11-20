import {
  createStyles,
  Image,
  Container,
  Title,
  Button,
  Group,
  Text,
  List,
  ThemeIcon,
} from "@mantine/core";
import { IconCheck } from "@tabler/icons";
import image from "./image.png";

const useStyles = createStyles((theme) => ({
  inner: {
    display: "flex",
    justifyContent: "space-between",
    paddingTop: theme.spacing.xl * 4,
    paddingBottom: theme.spacing.xl * 4,
  },

  content: {
    maxWidth: 480,
    marginRight: theme.spacing.xl * 3,

    [theme.fn.smallerThan("md")]: {
      maxWidth: "100%",
      marginRight: 0,
    },
  },

  title: {
    color: theme.colorScheme === "dark" ? theme.white : theme.black,
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: 44,
    lineHeight: 1.2,
    fontWeight: 900,

    [theme.fn.smallerThan("xs")]: {
      fontSize: 28,
    },
  },

  control: {
    [theme.fn.smallerThan("xs")]: {
      flex: 1,
    },
  },

  image: {
    flex: 1,

    [theme.fn.smallerThan("md")]: {
      display: "none",
    },
  },

  highlight: {
    position: "relative",
    backgroundColor: theme.fn.variant({
      variant: "light",
      color: theme.primaryColor,
    }).background,
    borderRadius: theme.radius.sm,
    padding: "4px 12px",
  },
}));

export function HeroBullets() {
  const { classes } = useStyles();
  return (
    <div>
      <Container>
        <div className={classes.inner}>
          <div className={classes.content}>
            <Title className={classes.title}>
              <span className={classes.highlight}>SNDB</span> Social Network
              Data Bridge
            </Title>
            <Text color="dimmed" mt="md">
              An interoperable social identity that bridges your established
              connections and reputation from web2 to web3
            </Text>

            <List
              mt={30}
              spacing="sm"
              size="sm"
              icon={
                <ThemeIcon size={20} radius="xl">
                  <IconCheck size={12} stroke={1.5} />
                </ThemeIcon>
              }
            >
              The biggest friction for people to adopt a new social network is
              the cold start problem - connections and reputations established
              on incumbent platforms are difficult to migrate. For regular
              people, it's hard to leave a social network where their friends
              are on. For creators, it's hard to leave their established
              followers for which they can monetize. <br />
              <br /> SNDB proposes to make social data on-boarding to web3 much
              more streamlined.
              <br />
              <br />
              <List.Item>
                User authenticates and grants SNDB permission to their own data
                on web2 incumbents, for which they have rights to.
              </List.Item>
              <List.Item>
                SNDB downloads user data and store on Filecoin encrypted. Data
                include username, profile pics, friend/follower graphs,
                published content.
              </List.Item>
              <List.Item>
                User can choose to publish to web3 Social Network. E.g. with a
                Lens protocol adapter, a user can mint a Lens profile populated
                with existing info from Twitter easily, and publishing some of
                the recent tweets.
              </List.Item>
              <List.Item>
                Content can be cross posted from web3 to web2 via making a
                request to SNDB which stores the user auth token.
              </List.Item>
              <List.Item>Earn SNDB tokens for migrating data!</List.Item>
            </List>

            <Group mt={30}>
              <Button
                component="a"
                href="https://github.com/nlnw/sndb/blob/main/README.md"
                target="_blank"
                radius="xl"
                size="md"
                className={classes.control}
              >
                Get started
              </Button>
              <Button
                component="a"
                href="https://github.com/nlnw/sndb"
                target="_blank"
                variant="default"
                radius="xl"
                size="md"
                className={classes.control}
              >
                Source code
              </Button>
            </Group>
          </div>
          <Image src={image} className={classes.image} />
        </div>
      </Container>
    </div>
  );
}
