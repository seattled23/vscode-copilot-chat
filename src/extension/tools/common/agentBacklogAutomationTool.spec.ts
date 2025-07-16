import { AgentBacklogAutomationTool, AgentBacklogAutomationInput } from './agentBacklogAutomationTool';

describe('AgentBacklogAutomationTool', () => {
  const tool = new AgentBacklogAutomationTool();

  it('should echo the input action and files', async () => {
    const input: AgentBacklogAutomationInput = { action: 'aggregate', files: ['file1.md', 'file2.md'] };
    const result = await tool.run(input, {} as any, {} as any);
    expect(result.output).toContain('aggregate');
    expect(result.output).toContain('file1.md');
    expect(result.output).toContain('file2.md');
  });

  it('should handle missing files gracefully', async () => {
    const input: AgentBacklogAutomationInput = { action: 'deduplicate' };
    const result = await tool.run(input, {} as any, {} as any);
    expect(result.output).toContain('deduplicate');
    expect(result.output).toContain('all');
  });
});
