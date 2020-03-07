/**
 * Created by Tomz on 4/21/2017.
 */

import javafx.animation.PathTransition;
import javafx.animation.Transition;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.scene.shape.Line;
import javafx.stage.Stage;
import javafx.scene.shape.Circle;
import javafx.util.Duration;

import java.util.ArrayList;

public class Hangman extends Application {

    ArrayList<Character> correct = new ArrayList<>();
    ArrayList<Character> incorrect = new ArrayList<>();
    int wrongGuess = 0;


    String[] words = {"write", "program", "that", "receive", "positive",
            "excellent", "linger", "violin", "strange", "holiday", "twilight",
            "school", "teacher", "tutor", "mother"};

    String hangWord = words[(int) (Math.random() * 10)];
    String mystery = "";
    PathTransition path;
    char letter;
    Label lbWord;

    @Override
    public void start(Stage primaryStage) {


        BorderPane pane = new BorderPane();


        Arc stand = new Arc(300, 450, 50, 50, 55, 70);
        stand.setType(ArcType.OPEN);
        stand.setStroke(Color.BLACK);


        Line top = new Line(300, 400, 300, 100);
        top.setStroke(Color.BLACK);

        Line wood = new Line(300, 100, 500, 100);
        wood.setStroke(Color.BLACK);

        Line choker = new Line(500, 100, 500, 150);
        choker.setStroke(Color.BLACK);

        Circle head = new Circle(500, 180, 30);
        head.setStroke(Color.BLACK);
        head.setFill(Color.TRANSPARENT);

        Line body = new Line(500, 210, 500, 350);
        body.setStroke(Color.BLACK);

        Line leftArm = new Line(500, 240, 450, 300);
        leftArm.setStroke(Color.BLACK);

        Line rightArm = new Line(500, 240, 550, 300);
        rightArm.setStroke(Color.BLACK);

        Line leftLeg = new Line(500, 350, 450, 400);
        leftLeg.setStroke(Color.BLACK);

        Line rightLeg = new Line(500, 350, 550, 400);
        rightLeg.setStroke(Color.BLACK);

        Label lbGuess = new Label("Guess a letter:");
        TextField tfGuess = new TextField();

        Label lbGameOver = new Label("GAME OVER. To continue game, press reset");
        Label lbContinue = new Label("To continue game, press reset.");
        Label lbAlreadyGuessed = new Label("Letter has already been guessed. Enter another letter.");

        HBox align = new HBox();
        align.setSpacing(10);

        Button reset = new Button("Reset Game");

        for (int i = 0; i < hangWord.length(); i++) {
            mystery += "*";
        }

        lbWord = new Label(mystery);
        align.getChildren().addAll(lbGuess, tfGuess, lbWord);
        pane.setBottom(align);

        pane.getChildren().addAll(wood, top, choker, stand);

        Label missed = new Label("");
        Label wrongLetters = new Label();

        align.getChildren().addAll(missed, wrongLetters);


        tfGuess.setOnAction(e -> {
            String guess = tfGuess.getText();

            if(path != null)
            {
                path.stop();
            }


            letter = guess.charAt(0);

            if(alreadyGuessed(letter))
            {
                pane.setCenter(lbAlreadyGuessed);
            }
            else if (!hangWord.contains("" + letter)) {
                wrongGuess += 1;
                missed.setText("Missed Letter: ");
                wrongLetters.setText(inCorrectLetter(hangWord, letter));
                pane.getChildren().remove(lbAlreadyGuessed);
                if (wrongGuess == 1) {
                    pane.getChildren().add(head);
                } else if (wrongGuess == 2) {
                    pane.getChildren().add(body);
                } else if (wrongGuess == 3) {
                    pane.getChildren().add(leftArm);
                } else if (wrongGuess == 4) {
                    pane.getChildren().add(rightArm);
                } else if (wrongGuess == 5) {
                    pane.getChildren().add(leftLeg);
                } else if (wrongGuess == 6) {
                    pane.getChildren().add(rightLeg);
                } else if (wrongGuess == 7) {

                    align.getChildren().add(lbGameOver);
                    animateHang(choker, head, body, leftArm, rightArm, leftLeg, rightLeg);
                    pane.setLeft(reset);
                }
            }
            else {
                lbWord.setText(correctLetter(hangWord, letter));
                pane.getChildren().remove(lbAlreadyGuessed);
                if (correctLetter(hangWord,letter).equals(hangWord)) {

                    align.getChildren().add(lbContinue);
                    pane.setLeft(reset);
                }
            }

        });

        reset.setOnAction(_e->{
            reset(pane,align,head,body,leftArm, rightArm,leftLeg, rightLeg, missed,
                    wrongLetters,lbContinue, lbGameOver, reset);
        });

        Scene scene = new Scene(pane, 700, 600);




        primaryStage.setTitle("Hangman");
        primaryStage.setScene(scene);
        primaryStage.show();

    }

    public static void main(String[] args) {
        launch(args);
    }

    public void reset(BorderPane pane, HBox align,  Circle head, Line body,Line leftArm,
                      Line rightArm, Line leftLeg, Line rightLeg, Label missed,
                      Label wrongLetters, Label lbContinue, Label lbGameOver, Button button)
    {
        if(path != null)
        {
            path.stop();
        }

        pane.getChildren().removeAll(head, body, rightArm, rightLeg, leftArm, leftLeg,button);
        align.getChildren().removeAll(lbContinue,lbGameOver);
        missed.setText("");
        wrongLetters.setText("");
        correct.clear();

        incorrect.clear();

        hangWord = words[(int) (Math.random() * 10)];
        mystery = "";
        wrongGuess = 0;
        for (int i = 0; i < hangWord.length(); i++) {
            mystery += "*";
        }



        lbWord.setText(mystery);

    }

    public String correctLetter(String word, char letter) {

        String progress = "";
        String guess = "" + letter;


        if (word.contains(guess)) {
            correct.add(letter);
        }
        else {
            incorrect.add(letter);
        }

        for (char c : word.toCharArray()) {
            if (correct.contains(c)) {
                progress += c;
            } else {
                progress += "*";
            }
        }

        return progress;
    }

    public String inCorrectLetter(String word, char letter) {

        String progress = "";
        String guess = "" + letter;

        if(incorrect.contains(letter))
        {
            progress = "Letter was already guessed. Enter in another letter.";
        }
        else if (word.contains(guess)) {
            correct.add(letter);
        }
        else {
            incorrect.add(letter);
        }

        for (int i = 0; i < incorrect.size(); i++) {
            progress += incorrect.get(i);
        }


        return progress;
    }

    public boolean alreadyGuessed(char letter)
    {
        boolean guessed = false;
        if(correct.contains(letter) || incorrect.contains(letter))
        {
            guessed = true;
        }

        return guessed;
    }




    private void animateHang(Line line, Circle head, Line body,Line leftArm, Line rightArm, Line leftLeg, Line rightLeg) {


        head.translateXProperty().addListener((observable, oldValue, newValue) -> {
            body.setTranslateX(newValue.doubleValue());
            leftArm.setTranslateX(newValue.doubleValue());
            rightArm.setTranslateX(newValue.doubleValue());
            leftLeg.setTranslateX(newValue.doubleValue());
            rightLeg.setTranslateX(newValue.doubleValue());
        });

        head.translateYProperty().addListener((observable, oldValue, newValue) -> {
            body.setTranslateY(newValue.doubleValue());
            leftArm.setTranslateY(newValue.doubleValue());
            rightArm.setTranslateY(newValue.doubleValue());
            leftLeg.setTranslateY(newValue.doubleValue());
            rightLeg.setTranslateY(newValue.doubleValue());
        });


        Arc arc = new Arc(line.getEndX(), line.getEndY() + head.getRadius() - 10, 20, 10, 220, 85);
        arc.setFill(Color.TRANSPARENT);
        arc.setStroke(Color.BLACK);
        path = new PathTransition(Duration.seconds(3), arc, head);
        path.setCycleCount(Transition.INDEFINITE);
        path.setAutoReverse(true);
        path.setOrientation(PathTransition.OrientationType.ORTHOGONAL_TO_TANGENT);
        path.play();
    }
}
