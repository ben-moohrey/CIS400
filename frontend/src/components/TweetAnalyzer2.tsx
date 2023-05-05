import React, { useState } from 'react';
import { Container, Row, Col, Form, Button, Card, CardGroup, Spinner } from 'react-bootstrap';
import api from '../utility/api';
import { cyrb53 } from '../utility/tools'

function TweetAnalyzer2() {
  const [twitterHandle, setTwitterHandle] = useState('');
  const [prompt, setPrompt] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setResults([]);
    try {
      const response = await api.post('/analyze', { twitter_handle: twitterHandle, prompt: prompt });
      setResults(response.data.results);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Row className="justify-content-center mt-5">
        <Col xs={12} md={6}>
          <h1 className="text-center mb-4">Tweet-GPT</h1>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="twitterHandle">
              <Form.Label>Twitter Handle</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Twitter handle"
                value={twitterHandle}
                onChange={(e) => setTwitterHandle(e.target.value)}
              />
            </Form.Group>
            <Form.Group controlId="prompt">
              <Form.Label>Prompt</Form.Label>
              <Form.Control
                as="textarea"
                rows={3}
                placeholder="Enter prompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
              />
            </Form.Group>
            <Button variant="primary" type="submit" className="w-100" disabled={loading}>
              {loading ? (
                <>
                  <Spinner animation="border" size="sm" role="status" aria-hidden="true" />
                  <span className="ml-2">Loading...</span>
                </>
              ) : (
                'Analyze'
              )}
            </Button>
          </Form>
          {results.length > 0 && (
            <div>
                {results.map((result, index) => (
                <Card 
                    key={cyrb53(result)} 
                    className="p-2 mt-1"
                >
                    <Card.Title> Tweet {index+1} </Card.Title>
                    <Card.Text>{result}</Card.Text>
                </Card>
              ))
              }
            </div>
          )}
        </Col>
      </Row>
    </Container>
  );
}

export default TweetAnalyzer2;
